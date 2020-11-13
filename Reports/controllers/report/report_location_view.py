from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from Reports.dal.report_location_dal import ReportLocationDal
from Reports.responses.error_responses import ErrorResponses
from Reports.serializers.report.report_locations_serializer import ReportLocationsSerializer



class ReportLocationView(APIView):
    http_method_names = ['get',]
    report_location_dal = ReportLocationDal()
    err_res = ErrorResponses()

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.err_res.UNAUTHORIZED
        query_set = self.report_location_dal.get_all()
        paginator = LimitOffsetPagination()
        paginated_data = paginator.paginate_queryset(query_set, request)
        res_data = ReportLocationsSerializer(paginated_data, many=True).data

        return paginator.get_paginated_response(res_data)
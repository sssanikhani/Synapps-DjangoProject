from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from Reports.dal.report_type_dal import ReportTypeDal
from Reports.serializers.report.report_type_serializer import ReportTypeSerializer
from Reports.responses.error_responses import ErrorResponses


class ReportTypeView(APIView):
    http_method_names = ['get',]
    report_type_dal = ReportTypeDal()
    err_res = ErrorResponses()

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.err_res.UNAUTHORIZED
        parameters = request.GET
        limit = parameters.get('limit')
        if limit is not None:
            if not 10 <= int(limit) <= 100:
                return self.err_res.BAD_PAGINATION
        query_set = self.report_type_dal.get_all()
        paginator = LimitOffsetPagination()
        paginated_data = paginator.paginate_queryset(query_set, request)
        print(paginated_data)
        res_data = ReportTypeSerializer(paginated_data, many=True).data
        return paginator.get_paginated_response(res_data)
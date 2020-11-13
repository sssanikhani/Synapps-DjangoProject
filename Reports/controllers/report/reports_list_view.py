from rest_framework.views import APIView
from Reports.responses.error_responses import ErrorResponses
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status
from Reports.dal.report_dal import ReportDal
from Reports.serializers.report.report_deep_serializer import ReportDeepSerializer


class ReportView(APIView):
    http_method_names = [ 'get', 'post', ]
    err_res = ErrorResponses()

    def get(self, request, *args, **kwargs):
        queries = request.GET
        user = request.user
        if not user.is_authenticated:
            return self.err_res.UNAUTHORIZED

        type_id = queries.get('report_type_id')

        paginator = LimitOffsetPagination()

        report_dal = ReportDal()
        if type_id is None:
            query_data = paginator.paginate_queryset(report_dal.get_all(sorted_by='report_time'), request)
        else:
            query_data = paginator.paginate_queryset(report_dal.get_by_type(sorted_by='report_time'), request)
        
        reports_data = ReportDeepSerializer(query_data, many=True).data

        return paginator.get_paginated_response(reports_data)

    def post(self, request, *args, **kwargs):
        pass
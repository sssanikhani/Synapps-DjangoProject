from rest_framework.views import APIView
from Reports.responses.error_responses import ErrorResponses
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework import status
from Reports.dal.report.report_dal import ReportDal
from Reports.serializers.report.report_serializers import ReportDeepSerializer, ReportSerializer

class ReportView(APIView):
    http_method_names = [ 'get', 'post', ]
    err_res = ErrorResponses()
    report_dal = ReportDal()

    def get(self, request, *args, **kwargs):
        parameters = request.GET
        user = request.user
        if not user.is_authenticated:
            return self.err_res.UNAUTHORIZED

        limit = parameters.get('limit')
        if limit is not None:
            if not 10 <= int(limit) <= 100:
                return self.err_res.BAD_PAGINATION

        type_id = parameters.get('report_type_id')

        paginator = LimitOffsetPagination()

        report_dal = ReportDal()
        if type_id is None:
            query_data = paginator.paginate_queryset(
                self.report_dal.get_all(sorted_by='report_time'),
                request
            )
        else:
            query_data = paginator.paginate_queryset(
                report_dal.get_by_type(type_id, sorted_by='report_time'),
                request
            )
        
        reports_data = ReportDeepSerializer(query_data, many=True).data
        if not reports_data:
            return self.err_res.REPORT_NOT_FOUND

        return paginator.get_paginated_response(reports_data)

    def post(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return self.err_res.UNAUTHORIZED
        
        given_data = request.data
        serializer = ReportSerializer(data=given_data)
        valid = serializer.is_valid()
        if not valid:
            raise ParseError(serializer.errors)
        instance = serializer.save(submitter=user)
        res_data = ReportDeepSerializer(instance=instance).data
        return Response(
            status=status.HTTP_200_OK,
            data=res_data    
        )



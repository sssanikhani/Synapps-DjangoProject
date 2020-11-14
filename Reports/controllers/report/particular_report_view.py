from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework import status
from Reports.responses.error_responses import ErrorResponses
from Reports.dal.report.report_dal import ReportDal
from Reports.serializers.report.report_serializers import (
        ReportDeepSerializer,
        ReportSerializer
)


class ParticularReportView(APIView):
    http_method_names = ['get', 'put', 'delete',]
    err_res = ErrorResponses()
    report_dal = ReportDal()

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return self.err_res.UNAUTHORIZED
        report_id = int(kwargs.get('report_id'))
        report = self.report_dal.get_by_id(report_id)
        if report is not None and report.submitter != user:
            return self.err_res.FORBIDDEN
        if report is None:
            return self.err_res.REPORT_NOT_FOUND
        res_data = ReportDeepSerializer(report).data
        return Response(
            status=status.HTTP_200_OK,
            data=res_data
        )

    def delete(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return self.err_res.UNAUTHORIZED
        report_id = int(kwargs.get('report_id'))
        report = self.report_dal.get_by_id(report_id)
        if report is not None and report.submitter != user:
            return self.err_res.FORBIDDEN
        if report is None:
            return self.err_res.REPORT_NOT_FOUND
        
        report.delete()
        res = {
            'message': "report deleted successfully"
        }
        return Response(status=status.HTTP_200_OK, data=res)
    
    def put(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return self.err_res.UNAUTHORIZED
        
        report_id = int(kwargs.get('report_id'))
        report = self.report_dal.get_by_id(report_id)
        if report is not None and report.submitter != user:
            return self.err_res.FORBIDDEN
        if report is None:
            return self.err_res.REPORT_NOT_FOUND
        
        given_data = request.data
        serializer = ReportSerializer(report, data=given_data)
        valid = serializer.is_valid()
        if not valid:
            raise ParseError(serializer.errors)
        instance = serializer.save()
        res_data = ReportDeepSerializer(instance=instance).data
        return Response(
            status=status.HTTP_200_OK,
            data=res_data    
        )
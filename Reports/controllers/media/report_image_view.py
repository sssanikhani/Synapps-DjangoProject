import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotAcceptable
from Reports.entities.media.report_image_model import ReportImage
from Reports.responses.error_responses import ErrorResponses
from Reports.dal.report.report_dal import ReportDal
from Reports.dal.media.report_image_dal import ReportImageDal
from Reports.serializers.media.report_image_serializer import AddReportImageSerializer
from Reports.serializers.report.report_serializers import ReportDeepSerializer


class ReportAddImageView(APIView):
    LIMIT_FILE_SIZE = 20 * 10 ** 6 # 20 MB
    http_method_names = ['post',]
    err_res = ErrorResponses()
    report_dal = ReportDal()
    report_image_dal = ReportImageDal()

    def post(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return self.err_res.UNAUTHORIZED

        report_id = kwargs.get('report_id')

        report = self.report_dal.get_by_id(report_id)
        if not report:
            return self.err_res.REPORT_NOT_FOUND

        if report.submitter != user:
            return self.err_res.FORBIDDEN

        given_data = request.data
        file = given_data.get('image')
        if not file:
            return self.err_res.BAD_REQUEST
        
        if file.size > self.LIMIT_FILE_SIZE:
            return self.err_res.NOT_ACCEPTABLE

        print(given_data)
        serializer = AddReportImageSerializer(data=given_data)
        valid = serializer.is_valid()
        if not valid:
            raise NotAcceptable(serializer.errors)

        serializer.save(report=report)
        report = self.report_dal.get_by_id(report_id)
        res_data = ReportDeepSerializer(report).data

        return Response(
            status=status.HTTP_200_OK,
            data=res_data
        )
    
        



class ReportDeleteImageView(APIView):
    http_method_names = ['delete',]
    err_res = ErrorResponses()
    report_dal = ReportDal()
    report_image_dal = ReportImageDal()

    def delete(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return self.err_res.UNAUTHORIZED
        
        report_id = kwargs.get('report_id')
        image_id = kwargs.get('image_id')
        image = self.report_image_dal.get_by_id(image_id)
        if not image:
            return self.err_res.NOT_FOUND
        if image.report.id != report_id:
            return self.err_res.NOT_ACCEPTABLE
        if image.report.submitter != user:
            return self.err_res.FORBIDDEN
        
        if os.path.isfile(image.file.path):
            os.remove(image.file.path)

        image.delete()
        res = {
            'message': "Image deleted successfully"
        }

        return Response(
            status=status.HTTP_200_OK,
            data=res
        )
        
        

        
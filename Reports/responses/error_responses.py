from rest_framework.response import Response
from rest_framework import status


class ErrorResponses:
    @staticmethod
    def _err_unauthorized():
        error = {
            'code': "E_UNAUTHORIZED",
            'message': "شما باید با حساب کاربری خود وارد شوید."
        }
        return Response(status=status.HTTP_401_UNAUTHORIZED, data=error)
    
    @staticmethod
    def _err_forbidden():
        error = {
            'code': "E_FORBIDDEN",
            'message': "you are not allowed to perform this action"
        }
        return Response(status=status.HTTP_403_FORBIDDEN, data=error)
    
    @staticmethod
    def _err_report_not_found():
        error = {
            'code': "E_REPORT_NOT_FOUND",
            'message': "report not found with this id"
        }
        return Response(status=status.HTTP_404_NOT_FOUND, data=error)

    Unauthorized = _err_unauthorized
    Forbidden = _err_forbidden
    ReportNotFound = _err_report_not_found
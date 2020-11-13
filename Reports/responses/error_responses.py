from rest_framework.response import Response
from rest_framework import status


class ErrorResponses:

    def __init__(self):
        self.UNAUTHORIZED = self._err_unauthorized()
        self.FORBIDDEN = self._err_forbidden()
        self.REPORT_NOT_FOUND = self._err_report_not_found()
        self.BAD_REQUEST = self._err_bad_request()
        self.BAD_PAGINATION = self._err_bad_pagination()

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

    @staticmethod
    def _err_bad_request():
        error = {
            'code': "E_BAD_REQUEST",
            'message': "some parameters are not in true form"
        }
        return Response(status=status.HTTP_400_BAD_REQUEST, data=error)

    @staticmethod
    def _err_bad_pagination():
        error = {
            'code': "E_BAD_PAGINATION",
            'message': "limit or offset or both parameters are wrong"
        }
        return Response(status=status.HTTP_400_BAD_REQUEST, data=error)
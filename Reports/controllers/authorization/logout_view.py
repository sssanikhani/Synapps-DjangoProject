from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework import status
from Reports.responses.error_responses import ErrorResponses


class LogoutView(APIView):
    http_method_names = ['post',]
    err_res = ErrorResponses()

    def post(self, request, *args, **kwargs):
        refresh_token = request.data['refresh']

        try:
            token = RefreshToken(refresh_token)
        except TokenError:
            return self.err_res.UNAUTHORIZED


        token.blacklist()

        return Response(status=status.HTTP_200_OK)
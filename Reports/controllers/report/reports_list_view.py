from rest_framework.views import APIView
from Reports.responses.error_responses import ErrorResponses


class ReportView(APIView):
    http_method_names = [ 'get', 'post', ]

    def get(self, request, *args, **kwargs):
        queries = request.GET
        user = request.user
        if not user.is_authenticated:
            return ErrorResponses.Unauthorized
        type_id = queries.get('report_type_id')
        report_manager = ReportManager()
        if type_id is None:
            report_manager.get_all(sorted='reported')
        else:
            report_manager.get_by_type(sorted='reported')

    def post(self, request, *args, **kwargs):
        pass
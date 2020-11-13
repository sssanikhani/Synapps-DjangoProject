from Reports.entities.report.report_model import Report


class ReportManager:
    model = Report

    def get_by_type(self, type_id):
        query_set = self.model.objects.filter(report_type__id = type_id)
        return query_set
    
    def get_all(self):
        query_set = self.model.objects.all()
        return query_set
        
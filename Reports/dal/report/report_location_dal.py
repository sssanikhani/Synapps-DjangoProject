from Reports.entities.report.report_location_model import ReportLocation


class ReportLocationDal:
    model = ReportLocation

    def get_all(self, sorted_by=None):
        query_set = self.model.objects.all()
        if sorted_by is not None:
            return query_set.order_by(sorted_by)
        return query_set
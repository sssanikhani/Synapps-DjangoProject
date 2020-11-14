from Reports.entities.report.report_location_model import ReportLocation


class ReportLocationDal:
    model = ReportLocation

    def get_all(self, sorted_by=None):
        query_set = self.model.objects.all()
        if sorted_by is not None:
            return query_set.order_by(sorted_by)
        return query_set

    def create_or_update(self, id, name):
        location_qs = self.model.objects.filter(pid=id)
        if not location_qs:
            location_ = self.model.objects.create(
                pid=id,
                name=name
            )
        else:
            location_ = location_qs[0]
            location_.pid = id
            location_.name = name
            location_.save()
        return location_
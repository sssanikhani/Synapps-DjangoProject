from Reports.entities.report.report_type_model import ReportType


class ReportTypeDal:
    model = ReportType

    def get_all(self, sorted_by=None):
        query_set = self.model.objects.all()
        if sorted_by is not None:
            return query_set.order_by(sorted_by)
        return query_set

    def create_or_update(self, id, name):
        type_qs = self.model.objects.filter(pid=id)
        if not type_qs:
            type_ = self.model.objects.create(
                pid=id,
                name=name
            )
        else:
            type_ = type_qs[0]
            type_.pid = id
            type_.name = name
            type_.save()
        return type_
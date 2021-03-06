from Reports.entities.report.report_model import Report


class ReportDal:
    model = Report

    def get_by_type(self, type_id, sorted_by=None):
        query_set = self.model.objects.filter(report_type__pid = type_id)
        if sorted_by is not None:
            query_set = query_set.order_by(sorted_by)
        return query_set
    
    def get_all(self, sorted_by=None):
        query_set = self.model.objects.all()
        if sorted_by is not None:
            query_set = query_set.order_by(sorted_by)
        return query_set

    def get_by_id(self, id_):
        query_set = self.model.objects.filter(id=id_)
        if not query_set:
            return None
        return query_set[0]

    def delete_by_id(self, id_):
        query_set = self.model.objects.filter(id=id_)
        if not query_set:
            return None
        return query_set.delete()
        
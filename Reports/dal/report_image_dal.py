from Reports.entities.media.report_image_model import ReportImage


class ReportImageDal:
    model = ReportImage

    def get_by_report_id(self, report_id, sorted_by=None):
        query_set = self.model.objects.filter(report__id=report_id)
        if not sorted_by:
            return query_set.order_by(sorted_by)
        return query_set

    def get_by_id(self, id_):
        query_set = self.model.objects.filter(id=id_)
        if not query_set:
            return None
        return query_set[0]
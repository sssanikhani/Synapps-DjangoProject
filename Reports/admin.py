from django.contrib import admin
from Reports.entities.report.report_model import Report
from Reports.entities.report.report_type_model import ReportType
from Reports.entities.report.report_location_model import ReportLocation


class ReportAdmin(admin.ModelAdmin):
    pass

class ReportTypeAdmin(admin.ModelAdmin):
    pass

class ReportLocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Report, ReportAdmin)
admin.site.register(ReportType, ReportTypeAdmin)
admin.site.register(ReportLocation, ReportLocationAdmin)


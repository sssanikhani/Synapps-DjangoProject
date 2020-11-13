from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from Reports.controllers.authorization.logout_view import LogoutView
from Reports.controllers.report.reports_list_view import ReportView
from Reports.controllers.report.particular_report_view import ParticularReportView
from Reports.controllers.report.report_type_view import ReportTypeView
from Reports.controllers.report.report_location_view import ReportLocationView

authorization_urlpatterns = [

    # POST
    path('user/auth/token/', jwt_views.TokenObtainPairView.as_view(), name='pair token'),
    
    # POST
    path('user/auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh token'),
    
    # POST
    path('user/auth/logout/', LogoutView.as_view(), name='logout'),

]

report_urlpatterns = [

    # POST, GET
    path('report/', ReportView.as_view(), name='reports'),
    
    # GET, DELETE, PUT
    path('report/<int:report_id>/', ParticularReportView.as_view(), name='particular report'),

    # POST
    # path('report/<int:report_id>/image/', , name='upload report image'),

    #DELETE
    # path('report/<int:report_id>/image/<int:image_id>/', , name='delete image'),

    #GET
    path('report/type/', ReportTypeView.as_view(), name='report types'),

    #GET
    path('report/location/', ReportLocationView.as_view(), name='report locations'),

]


urlpatterns = [
    *authorization_urlpatterns,
    *report_urlpatterns,
]
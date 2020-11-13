from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from Reports.controllers.authorization.logout_view import LogoutView
from Reports.controllers.report.reports_list_view import ReportView

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
    
    # # GET, DELETE, PUT
    # path('report/<int:report_id>/', , name='particular report'),

    # # POST
    # path('report/<int:report_id>/image/', , name='upload report image'),

    # #DELETE
    # path('report/<int:report_id>/image/<int:image_id>/', , name='delete image'),

    # #GET
    # path('report/type/', , name='report types'),

    # #GET
    # path('report/location/', , name='report locations'),

]


urlpatterns = [
    *authorization_urlpatterns,
    *report_urlpatterns,
]
from rest_framework.serializers import ModelSerializer
from Reports.serializers.base_serializer import BaseSerializer
from Reports.entities.report.report_location_model import ReportLocation


class ReportLocationsSerializer(ModelSerializer, BaseSerializer):
    
    class Meta:
        model = ReportLocation
        fields = (
            'pid',
            'name',
        )
from rest_framework.serializers import ModelSerializer
from Reports.serializers.base_serializer import BaseSerializer
from Reports.entities.report.report_type_model import ReportType


class ReportTypeSerializer(ModelSerializer, BaseSerializer):
    
    class Meta:
        model = ReportType
        fields = (
            'pid',
            'name',
        )
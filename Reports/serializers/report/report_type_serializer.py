from rest_framework import serializers
from Reports.entities.report.report_type_model import ReportType


class ReportTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReportType
        fields = (
            'id',
            'name',
        )
    id = serializers.CharField(source='pid')


class ReportTypeShallowSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportType
        fields = (
            'id'
        )
    id = serializers.CharField(source='pid')
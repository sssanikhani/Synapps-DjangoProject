from rest_framework import serializers
from Reports.entities.report.report_location_model import ReportLocation


class ReportLocationsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReportLocation
        fields = (
            'id',
            'name',
        )
    id = serializers.CharField(source='pid')


class ReportLocationShallowSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReportLocation
        fields = (
            'id'
        )
    id = serializers.CharField(source='pid')
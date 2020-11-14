from rest_framework import serializers
from Reports.entities.report.report_model import Report
from Reports.entities.report.report_location_model import ReportLocation
from Reports.entities.report.report_type_model import ReportType
from Reports.serializers.report.report_type_serializer import (
    ReportTypeSerializer,
    ReportTypeShallowSerializer
)
from Reports.serializers.report.report_locations_serializer import (
    ReportLocationsSerializer, 
    ReportLocationShallowSerializer,
)
from Reports.serializers.media.report_image_serializer import ReportImageSerializer
from Reports.serializers.authorization.user_shallow_serializer import UserShallowSerializer


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = (
            'report_type_id',
            'location_ids',
            'content',
            'reported',
            'requester',
            'provider',
        )

    report_type_id = serializers.PrimaryKeyRelatedField(source='report_type', queryset=ReportType.objects.all())
    location_ids = serializers.PrimaryKeyRelatedField(many=True, source='report_locations', queryset=ReportLocation.objects.all())
    reported = serializers.DateTimeField(source='report_time')


class ReportDeepSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Report
        fields = (
            'id',
            'submitter',
            'report_type',
            'locations',
            'content',
            'reported',
            'requester',
            'provider',
            'images',
        )

    submitter = UserShallowSerializer(read_only=True)
    report_type = ReportTypeSerializer(read_only=True)
    locations = ReportLocationsSerializer(read_only=True, many=True, source='report_locations')
    reported = serializers.DateTimeField(source='report_time')
    images = ReportImageSerializer(many=True)
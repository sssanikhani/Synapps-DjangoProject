from rest_framework.serializers import ModelSerializer
from Reports.serializers.base_serializer import BaseSerializer
from Reports.entities.report.report_model import Report
from Reports.serializers.report.report_type_serializer import ReportTypeSerializer
from Reports.serializers.report.report_locations_serializer import ReportLocationsSerializer
from Reports.serializers.authorization.user_shallow_serializer import UserShallowSerializer


class ReportDeepSerializer(ModelSerializer, BaseSerializer):
    class Meta:
        model = Report
        fields = (
            'id',
            'submitter',
            'report_type',
            'report_locations',
            'content',
            'report_time',
            'requester',
            'provider',
        )
    submitter = UserShallowSerializer(read_only=True)
    report_type = ReportTypeSerializer(read_only=True)
    report_locations = ReportLocationsSerializer(read_only=True, many=True)
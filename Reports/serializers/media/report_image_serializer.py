from rest_framework import serializers
from Reports.entities.media.report_image_model import ReportImage
from Reports.entities.report.report_model import Report


class AddReportImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportImage
        fields = (
            'image',
        )
    image = serializers.ImageField(source='file')


class ReportImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportImage
        fields = (
            'id',
            'url',
        )
    url = serializers.FileField(read_only=True, source='file')
    
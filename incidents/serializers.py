from rest_framework import serializers
from .models import Incident


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ['id', 'title', 'latitude', 'longitude', 'created_at', 'status']
        read_only_fields = ['id', 'created_at']

    def validate_latitude(self, value):
        if value < -90 or value > 90:
            raise serializers.ValidationError("Широта повинна бути між -90 та 90")
        return value

    def validate_longitude(self, value):
        if value < -180 or value > 180:
            raise serializers.ValidationError("Довгота повинна бути між -180 та 180")
        return value


class GeoJSONSerializer(serializers.ModelSerializer):
    geometry = serializers.SerializerMethodField()
    properties = serializers.SerializerMethodField()

    class Meta:
        model = Incident
        fields = ['geometry', 'properties']

    def get_geometry(self, obj):
        return {
            "type": "Point",
            "coordinates": [float(obj.longitude), float(obj.latitude)]
        }

    def get_properties(self, obj):
        return {
            "id": obj.id,
            "title": obj.title,
            "status": obj.status,
            "created_at": obj.created_at.isoformat()
        }
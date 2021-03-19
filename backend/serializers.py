from rest_framework import serializers
from django.core.validators import FileExtensionValidator
from .models import RailInfo


class RailInfoCSVSerializer(serializers.Serializer):
    csv_file = serializers.FileField(
        write_only=True, validators=[FileExtensionValidator(["csv"])]
    )


class RailInfoSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    city = serializers.CharField()
    zone = serializers.IntegerField()
    division = serializers.IntegerField()
    connection = serializers.CharField()
    interchange = serializers.CharField()
    station = serializers.CharField()
    station_code = serializers.CharField()
    distance_in_km = serializers.FloatField()
    layout = serializers.CharField()
    parking_contract_available = serializers.CharField()
    space_available_no_contract = serializers.CharField()
    space_not_available = serializers.CharField()
    inserted_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = RailInfo
        fields = [
            "id",
            "city",
            "zone",
            "division",
            "connection",
            "interchange",
            "station",
            "station_code",
            "distance_in_km",
            "layout",
            "parking_contract_available",
            "space_available_no_contract",
            "space_not_available",
            "inserted_at",
            "updated_at",
        ]
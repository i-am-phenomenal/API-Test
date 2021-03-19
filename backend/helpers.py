from .models import *
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status


def create_rail_info(row):
    return RailInfo.objects.create(
        city=row["City"],
        zone=row["Zone"],
        division=row["Division"],
        connection=row["Connection"],
        interchange=row["Interchange"],
        station=row["Station"],
        station_code=row["Station Code"],
        distance_in_km=row["Distance in Kms"],
        layout=row["Layout"],
        parking_contract_available=row["Parking Contract Available"],
        space_available_no_contract=row["Space Avaiable No Contract"],
        space_not_available=row["Sapce Not Avaiable"],
        inserted_at=datetime.utcnow(),
    )


def create_bulk_rail_info(data_frame):
    objects = []
    for index, row in data_frame.iterrows():
        objects.append(create_rail_info(row))
    return objects


def get_railinfo_by_station(station):
    return RailInfo.objects.filter(station=station)


def validate_existence(fn):
    validate = lambda station_code: RailInfo.objects.filter(
        station_code=station_code
    ).exists()

    def inner_fn(self, request, *args, **kwargs):
        _from = request.GET.get("from")
        to = request.GET.get("to")
        success_cond = validate(_from) and validate(to)
        return (
            fn(self, request, _from, to)
            if success_cond
            else Response("Values do not exist", status.HTTP_404_NOT_FOUND)
        )

    return inner_fn


def get_distance(_from, to):
    get_distance_in_km = lambda station_code: RailInfo.objects.filter(
        station_code=station_code
    ).values_list("distance_in_km")[0][0]
    return abs(get_distance_in_km(_from) - get_distance_in_km(to))

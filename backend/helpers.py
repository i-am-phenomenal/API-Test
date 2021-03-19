from .models import *
from datetime import datetime


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
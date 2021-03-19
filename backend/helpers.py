from .models import *


def create_rail_info(index, data_frame):
    return RailInfo.objects.create(
        city=data_frame.loc[index, "City"],
        zone=data_frame.loc[index, "Zone"],
        division=data_frame.loc[index, "Division"],
        connection=data_frame.loc[index, "Connection"],
        interchange=data_frame.loc[index, "Interchange"],
        station=data_frame.loc["Station"],
        station_code=data_frame.loc["Station Code"],
        distance_in_km=data_frame.loc["Distance in Kms"],
        layout=data_frame.loc["Layout"],
        parking_contract_available=data_frame.loc["Parking Contract Available"],
        space_available_no_contract=data_frame.loc["Space Avaiable No Contract"],
        space_not_available=data_frame.loc["Sapce Not Avaiable"],
        inserted_at=datetime.utcnow(),
    )


def create_bulk_rail_info(data_frame):
    print(data_frame.to_dict(), "q1111111111111111")
    objects = []
    # for index,row in data_frame.iterrows():
    #     print(row[1])
    #     objects.append(create_rail_info(row[1], data_frame))
    return objects
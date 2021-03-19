from django.db import models
import uuid

# Create your models here.


class RailInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city = models.CharField(max_length=50, default="")
    zone = models.IntegerField(default=-1)
    division = models.IntegerField(default=-1)
    connection = models.CharField(max_length=100, default="")
    interchange = models.CharField(max_length=100, default="")
    station = models.CharField(max_length=100, default="")
    station_code = models.CharField(max_length=100, default="")
    distance_in_km = models.FloatField(default=0.0)
    layout = models.CharField(max_length=100, default="")
    parking_contract_available = models.CharField(max_length=10, default="")
    space_available_no_contract = models.CharField(max_length=10, default="")
    space_not_available = models.CharField(max_length=10, default="")
    insertedAt = models.DateTimeField(auto_now=True, db_column="inserted_at")
    updatedAt = models.DateTimeField(auto_now=True, db_column="updated_at")

    class Meta:
        db_table = "rail_infos"
from django.shortcuts import render
from rest_framework import generics
from .models import RailInfo
from rest_framework import authentication
import json
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .serializers import RailInfoCSVSerializer, RailInfoSerializer
from datetime import datetime
import pandas as pd
from . import helpers


class PermissionMixin:
    permission_classes = [AllowAny]


class ImportCSVAPIVIew(PermissionMixin, generics.CreateAPIView):
    """
    Generic view class for  importting RailInfo records from CSV

    Args:
        generics (Class): Generic API class
    """

    serializer_class = RailInfoCSVSerializer

    def perform_create(self, serialized):
        data_frame = pd.read_csv(
            serialized.validated_data.get("csv_file"),
            encoding="ISO-8859–1",
            sep=",",
            error_bad_lines=False,
        )
        return helpers.create_bulk_rail_info(data_frame)

    def create(self, request, *args, **kwargs):
        serialized = self.get_serializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        created_objects = self.perform_create(serialized)
        resp = RailInfoSerializer(created_objects, many=True)
        return Response(resp.data, status.HTTP_201_CREATED)


class RetreiveAllRailInfo(PermissionMixin, generics.ListAPIView):
    """
    Generic view class for GET (all) RailInfo records

    Args:
        generics (Class): Generic API class
    """

    serializer_class = RailInfoSerializer
    queryset = RailInfo.objects.all()


class RailInfoSearchAPIView(PermissionMixin, generics.ListAPIView):
    """
    Generic view class for GET (all) RailInfo records on the basis of station which is going to be passed through  query parameters

    Args:
        generics (Class): Generic API class
    """

    serializer_class = RailInfoSerializer

    def list(self, request, *args, **kwargs):
        print(request.GET.get("station"), "1111111111111111111")
        info = helpers.get_railinfo_by_station(request.GET.get("station"))
        resp = RailInfoSerializer(info, many=True)
        return Response(resp.data, status.HTTP_200_OK)

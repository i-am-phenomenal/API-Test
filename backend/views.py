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


class ImportCSVAPIVIew(generics.CreateAPIView):
    """
    Generic view class for  importting RailInfo records from CSV

    Args:
        generics (Class): Generic API class
    """

    permission_classes = [AllowAny]
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
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Incident
from .serializers import IncidentSerializer, GeoJSONSerializer


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        incidents = self.get_queryset()
        serializer = self.get_serializer(incidents, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        incident = get_object_or_404(Incident, pk=pk)
        serializer = self.get_serializer(incident)
        return Response(serializer.data)

    def update(self, request, pk=None):
        incident = get_object_or_404(Incident, pk=pk)
        serializer = self.get_serializer(incident, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        incident = get_object_or_404(Incident, pk=pk)
        serializer = self.get_serializer(incident, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        incident = get_object_or_404(Incident, pk=pk)
        incident.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def active_geojson(self, request):
        """Повертає активні інциденти у форматі GeoJSON"""
        active_incidents = Incident.objects.filter(status='active')
        features = []

        for incident in active_incidents:
            serializer = GeoJSONSerializer(incident)
            feature = {
                "type": "Feature",
                **serializer.data
            }
            features.append(feature)

        geojson = {
            "type": "FeatureCollection",
            "features": features
        }

        return Response(geojson)
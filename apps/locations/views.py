from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Location
from .serializers import LocationSerializer
from .services import LocationService


class LocationListCreateView(generics.ListCreateAPIView):
    """
    List all locations of the authenticated user
    or create a new location.
    """

    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Location.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        location = LocationService.create_location(
            user=self.request.user,
            validated_data=serializer.validated_data,
        )
        serializer.instance = location


class LocationRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView
):
    """
    Retrieve, Update or Delete a location.
    """

    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Location.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        LocationService.update_location(
            self.get_object(),
            serializer.validated_data,
        )

    def perform_destroy(self, instance):
        instance.soft_delete()
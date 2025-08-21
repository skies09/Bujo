from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from accounts.user_profile.serializers import (
    AffirmationSerializer,
    GratitudeSerializer,
    PassionSerializer,
    FavoriteThingSerializer,
    AboutSerializer,
    AboutSummarySerializer
)
from accounts.user_profile.models import Affirmation, Gratitude, Passion, FavoriteThing, About
from accounts.abstract.viewsets import AbstractViewSet


class AffirmationViewSet(AbstractViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AffirmationSerializer
    lookup_field = 'public_id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['text']
    ordering_fields = ['order', 'created', 'updated']
    ordering = ['order', 'created']

    def get_queryset(self):
        return Affirmation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GratitudeViewSet(AbstractViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = GratitudeSerializer
    lookup_field = 'public_id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['text']
    ordering_fields = ['order', 'created', 'updated']
    ordering = ['order', 'created']

    def get_queryset(self):
        return Gratitude.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PassionViewSet(AbstractViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PassionSerializer
    lookup_field = 'public_id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['text']
    ordering_fields = ['order', 'created', 'updated']
    ordering = ['order', 'created']

    def get_queryset(self):
        return Passion.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FavoriteThingViewSet(AbstractViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = FavoriteThingSerializer
    lookup_field = 'public_id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'is_active']
    search_fields = ['title', 'description']
    ordering_fields = ['category', 'order', 'created', 'updated']
    ordering = ['category', 'order', 'created']

    def get_queryset(self):
        return FavoriteThing.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AboutViewSet(AbstractViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AboutSerializer
    lookup_field = 'public_id'
    http_method_names = ('get', 'post', 'patch', 'delete')
    
    def get_queryset(self):
        return About.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_object(self):
        """Get or create About object for the user"""
        try:
            return About.objects.get(user=self.request.user)
        except About.DoesNotExist:
            # Create a new About object if it doesn't exist
            return About.objects.create(user=self.request.user)
    
    def list(self, request, *args, **kwargs):
        """Override list to return single object since it's OneToOneField"""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

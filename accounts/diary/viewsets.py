from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import Diary
from .serializers import DiaryEntrySerializer


class DiaryEntryViewSet(viewsets.ModelViewSet):
    serializer_class = DiaryEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"  # Enable UUID-based lookup

    def get_queryset(self):
        user = self.request.user
        queryset = Diary.objects.filter(user=user)

        filter_val = self.request.query_params.get("filter")
        date_str = self.request.query_params.get("date")
        today = timezone.now().date()

        if date_str:
            # Filter by specific date (YYYY-MM-DD)
            try:
                from datetime import datetime

                date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
                queryset = queryset.filter(date=date_obj)
            except Exception:
                pass  # Ignore invalid date format, return all
        elif filter_val == "week":
            start_date = today - timedelta(days=7)
            queryset = queryset.filter(date__gte=start_date, date__lte=today)
        elif filter_val == "month":
            start_date = today - timedelta(days=30)
            queryset = queryset.filter(date__gte=start_date, date__lte=today)
        elif filter_val == "3months":
            start_date = today - timedelta(days=90)
            queryset = queryset.filter(date__gte=start_date, date__lte=today)

        return queryset.order_by("-date_created")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from .models import Reminder
from rest_framework import viewsets
from .serializers import ReminderSerializer
from rest_framework.permissions import AllowAny


class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    permission_classes = [AllowAny]  # There is no authentication system

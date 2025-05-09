from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from reminder.views import ReminderViewSet

router = routers.DefaultRouter()
router.register(r'reminders',  ReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
]

from django.db import models


class Reminders(models.Model):
    message = models.CharField(max_length=512, blank=True)
    trigger_time = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return self.message

from django.db import models


class Reminder(models.Model):
    message = models.CharField(max_length=512, blank=True)
    trigger_time = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name_plural = "Reminders"

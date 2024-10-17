# schedule/models.py
from django.db import models

class TimeSlot(models.Model):
    day_of_week_choices = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    day_of_week = models.CharField(max_length=9, choices=day_of_week_choices)
    start_time = models.TimeField()
    stop_time = models.TimeField()
    ids = models.JSONField()  # To store a list of IDs associated with the time slot

    def __str__(self):
        return f"{self.day_of_week} {self.start_time}-{self.stop_time}"

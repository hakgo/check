from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

import datetime

class Meeting(models.Model):
    title = models.CharField(max_length=100)
    meeting_date = models.DateTimeField()

    def __str__(self):
        return self.title


class MeetingAttendance(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_date = models.DateTimeField(auto_now=True)

    def not_late(self):
        return self.check_date <= meeting.meeting_date

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('list')
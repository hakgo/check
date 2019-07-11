from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import *

class MeetingListView(ListView):
    model = Meeting
    template_name = 'home/list.html'

class CheckView(CreateView):
    model = MeetingAttendance
    fields = ['user']
    success_url = reverse_lazy('home')
    template_name = 'home/check.html'

class MeetingCreateView(CreateView):
    model = Meeting
    fields = ['title', 'meeting_date']
    template_name = 'home/create.html'
    success_url = reverse_lazy('home')
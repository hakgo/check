from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import *

def list_view(request):
    object_list = Meeting.objects.all()
    return render(request, 'home/list.html', {'object_list':object_list})


class MeetingListView(ListView):
    model = Meeting
    template_name = 'home/list.html'

    def not_late(self, idx):
        meeting = self.request.objects.get(pk=idx)
        return meeting.meetingattendance_set.check_date <= meeting.meeting_date

class CheckView(CreateView):
    model = MeetingAttendance
    fields = []
    success_url = reverse_lazy('home')
    template_name = 'home/check.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.meeting_id = self.kwargs['pk']
        return super().form_valid(form)

class MeetingCreateView(CreateView):
    model = Meeting
    fields = ['title', 'meeting_date']
    template_name = 'home/create.html'
    success_url = reverse_lazy('home')

class MeetingDetailView(ListView):
    model = MeetingAttendance
    template_name = 'home/detail.html'
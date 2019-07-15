from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import *

def list_view(request):
    object_list = Meeting.objects.all()
    return render(request, 'home/list.html', {'object_list':object_list})

def detail_view(request, pk):
    meeting = Meeting.objects.get(pk=pk)
    return render(request, 'home/detail.html', {'meeting':meeting})

class CheckView(CreateView):
    model = MeetingAttendance
    fields = []
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

class UserListView(ListView):
    model = MeetingAttendance
    template_name = 'home/user_list.html'
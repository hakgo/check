from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *


urlpatterns = [
    path('', list_view, name='home'),
    path('check/<int:pk>/', login_required(CheckView.as_view()), name='check'),
    path('create/', login_required(MeetingCreateView.as_view()), name='create'),
    path('detail/<int:pk>/', MeetingDetailView.as_view(), name='detail'),
]
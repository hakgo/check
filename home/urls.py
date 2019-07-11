from django.urls import path

from .views import *

urlpatterns = [
    path('', MeetingListView.as_view(), name='home'),
    path('check/<int:pk>/', CheckView.as_view(), name='check'),
    path('create/', MeetingCreateView.as_view(), name='create'),
]
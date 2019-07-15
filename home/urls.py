from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *


urlpatterns = [
    path('', list_view, name='home'),
    path('detail/<int:pk>/', detail_view, name='detail'),
    path('check/<int:pk>/', login_required(CheckView.as_view()), name='check'),
    path('create/', login_required(MeetingCreateView.as_view()), name='create'),
    path('user_list/<int:pk>/', UserListView.as_view(), name='user_list'),
]
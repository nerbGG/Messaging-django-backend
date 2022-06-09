"""messagingbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from api import views as api_views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', auth_views.obtain_auth_token,name='api_token_auth'),
    path('login/',api_views.login_view),
    path('', api_views.api_over_view),
    # path('messages/', api_views.message_list_view),
    # path('messages_to/<recipient_id>/', api_views.messages_to),
    path('create-message/', api_views.create_message),
    path('room/all/<user_id>/',api_views.get_all_rooms),
    path('create-room/',api_views.create_room),
    path('room/<room_id>/messages/', api_views.get_room_messages),
    path('room/adduser/',api_views.add_user),
]

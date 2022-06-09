from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .models import Message, Room
# , MessageThrough
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .serializers import MessageSerializer, UserSerializer, RoomSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# url = 'http://127.0.0.1:8000//'
# headers = {'Authorization': 'Token 9054f7aa9305e012b3c2300408c3dfdf390fcddf'}
# r = requests.post(url, headers=headers)

# {
#   "username": "nerb",
#   "password":1234
# }

# , MessageThroughSerializer
@api_view(['POST'])
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/api/')
    # serializer = UserSerializer(data=request.data)
    username = request.data['username']
    pss = request.data['password']
    user = authenticate(request, username=username, password=pss)
    if user is not None:
        login(request, user)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    else:
        value = {"authenticated": False}
        return Response(value)


# Create your views here.
# @login_required(login_url='/api/login/')
@api_view(['GET'])
def api_over_view(request):
    api_urls = {
        # 'user_messages': '/messages/',  # all the user's messages
        # 'messages_to': '/messages/<str:recipient_id>/',  # all the user's messages to a person
        'create message': '/create-message/',
        'delete': '/delete-message/<str:message_id>/',
        'all-rooms': '/room/all/<user_id>',  # all rooms that a user is a part of
        'create-room': '/create-room/',
        'room messages': '/room/<str:room_id>/messages/',  # all messages in that room
        'adduser': '/room/<str:room_id>/adduser/<str:user_id>/',  # adding a user to the room
        # 'message':'/messages/message/<str:id>',
    }
    return Response(api_urls)


# @login_required(login_url='/api/login')
@api_view(['GET'])
def room_messages(request, room_id):
    room = Room.objects.get(id=room_id)


# @login_required(login_url='/api/login/')
# @api_view(['GET'])
# def message_list_view(request):
#     # return all the user's messages'
#     messages = Message.objects.filter(author_id=request.user.id)
#     # return JsonResponse(messages, safe=False)
#     serializer = MessageSerializer(messages, many=True)
#     return Response(serializer.data)
#
#
# @login_required(login_url='/api/login/')
# @api_view(['GET'])
# def messages_to(request, recipient_id):
#     # return all the user's messages'
#     messages = Message.objects.filter(author_id=request.user.id, recipient_id=recipient_id)
#     # messages = MessageThrough.objects.filter(message__author_id=request.user.id)
#     # return JsonResponse(messages, safe=False)
#     serializer = MessageSerializer(messages, many=True)
#     return Response(serializer.data)


# @login_required(login_url='/api/login/')
@api_view(['POST'])
def create_message(request):
    serializer = MessageSerializer(data=request.data)
    # can user a serializer like a form to create message objects
    if serializer.is_valid():
        serializer.save()
    else:
        message_data = serializer.initial_data
        message = Message(author_id=message_data["author"], text=message_data["text"],
                          recipient_id=message_data["recipient"], room_id=message_data["room"])
        message.save()
    return Response(serializer.data)


# {
#         "author": 4,
#         "recipient":5,
#         "text": "sakndlakndkjnaskdjnkasdkankjdnksadnkjsdakjndskjankdjsjnakjdnknjasndk",
#         "time_sent": "2022-06-06T15:54:10Z"
#         "room": 1
# }
# @login_required(login_url='/api/login/')
@api_view(['POST'])
def create_room(request):
    serializer = RoomSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# @login_required(login_url='/api/login/')
@api_view(['GET'])
def get_room_messages(request, room_id):
    room = Room.objects.get(id=room_id)
    messages = Room.objects.get(id=room_id).message_set.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)


# @login_required(login_url='/api/login/')
@api_view(['GET'])
def get_all_rooms(request, user_id):
    user = User.objects.get(id=user_id)
    rooms = user.room_set.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


# @login_required(login_url='/api/login/')
@api_view(['POST'])
def add_user(request):
    serializer = RoomSerializer(data=request.data)
    room = Room.objects.get(id=request.data["room_id"])
    user = User.objects.get(id=request.data["user_id"])
    room.users.add(user)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)
# {
#   "user_id":5,
#    "room_id":2
# }

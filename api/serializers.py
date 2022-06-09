from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message, Room


# ,  MessageThrough


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class MessageSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False)
    # recipient = UserSerializer(many=False)

    class Meta:
        model = Message
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    class Meta:
        model = Room
        fields = '__all__'

# class MessageThroughSerializer(serializers.ModelSerializer):
#     # this allows for a nested json object, it will show the messages fields instead of just the id
#     message = MessageSerializer(many=False)
#     recipient = UserSerializer(many=False)
#
#     class Meta:
#         model = MessageThrough
#         fields = '__all__'

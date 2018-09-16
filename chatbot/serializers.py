'''
Created on Sep 9, 2018

@author: ingkotkar
'''
from datetime import datetime
from rest_framework import serializers

from models import Chatbot
from django.contrib.auth.models import User

class ChatbotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chatbot
        fields = ("id", "message", "creation_datetime", "sender", "receiver", "sender_name", "receiver_name",)

    def validate_message(self, value):
        if value == "":
            raise serializers.ValidationError("Message cannot be empty.")
        return value

    def create(self, validated_data):
        return Chatbot.objects.create(**validated_data)

class ChatbotUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username",)

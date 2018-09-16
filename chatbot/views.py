# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.viewsets import GenericViewSet
from serializers import ChatbotSerializer, ChatbotUserSerializer
from models import Chatbot
from django.contrib.auth.models import User

# Create your views here.
class ChatbotViewset(GenericViewSet, ListCreateAPIView):
    serializer_class = ChatbotSerializer

    def get_queryset(self):
        send_to, auth_user = self.kwargs.get("send_to"), self.request.META.get("HTTP_AUTHUSERID", '0')
        queryset = Chatbot.objects.filter(sender__id__in=[auth_user,
                                                          send_to],
                                          receiver__id__in=[auth_user,
                                                            send_to])
        return queryset.order_by("creation_datetime")

class ChatbotUsersViewset(GenericViewSet, ListAPIView):
    serializer_class = ChatbotUserSerializer

    def get_queryset(self):
        auth_user_id = self.request.META.get("HTTP_AUTHUSERID", '0')
        return User.objects.exclude(id=auth_user_id)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chatbot(models.Model):
    message = models.CharField(max_length=200)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, related_name="SendFrom", blank=True, null=True)
    receiver = models.ForeignKey(User, related_name="SendTo", blank=True, null=True)

    @property
    def sender_name(self):
        return self.sender.username

    @property
    def receiver_name(self):
        return self.receiver.username
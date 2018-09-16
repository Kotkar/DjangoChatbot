'''
Created on Sep 8, 2018

@author: gkotkar
'''
from django.conf.urls import url, include
from rest_framework import routers

from views import ChatbotViewset, ChatbotUsersViewset 


router = routers.DefaultRouter()
# router.register(r'chatbot', ChatbotViewset, base_name="chatbot")
router.register(r'(?P<send_to>\d+)', ChatbotViewset, base_name="user-specific-chatbot")
router.register(r'chatusers', ChatbotUsersViewset, base_name="user-specific-chatbot")
urlpatterns = router.urls

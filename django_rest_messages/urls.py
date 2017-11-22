from django.conf.urls import url, include
from django.views.generic import RedirectView
from api import router

from django_messages.views import *

urlpatterns = [
    url(r'^inbox/$', inbox, name='messages_inbox'),
    url(r'^outbox/$', outbox, name='messages_outbox'),
    url(r'^compose/$', compose, name='messages_compose'),
    url(r'^compose/(?P<recipient>[\w.@+-]+)/$', compose, name='messages_compose_to'),
    url(r'^reply/(?P<message_id>[\d]+)/$', reply, name='messages_reply'),
    url(r'^trash/$', trash, name='messages_trash'),

    # Defining the API endpoint
    url(r'^', include(router.urls)),
]

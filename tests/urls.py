from django.conf.urls import url, include


urlpatterns = [
    url(r'^messages/', include('django_rest_messages.urls')),
]

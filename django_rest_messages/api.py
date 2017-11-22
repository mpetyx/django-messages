from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, mixins
from models import Message


# Serializers define the API representation.
class MessageSerializer(serializers.ModelSerializer):
    # Subject = serializers.CharField(source='Subject')

    class Meta:
        model = Message
        fields = '__all__'

# ViewSets define the view behavior.
class MessageViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet,
                      mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'message', MessageViewSet)


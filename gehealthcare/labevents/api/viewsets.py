from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import (
	ItemSerializer, LabeventSerializer
)
from ..models import (
	Item, Labevent
)

class ItemViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	permission_class = (IsAuthenticated,)


class LabeventViewSet(viewsets.ModelViewSet):
	queryset = Labevent.objects.all()
	serializer_class = LabeventSerializer
	permission_class = (IsAuthenticated,)

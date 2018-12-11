from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import (
	IcCodeSerializer, DiagnosesSerializer
)
from ..models import (
	IcCode, Diagnoses
)

class IcCodeViewSet(viewsets.ModelViewSet):
	queryset = IcCode.objects.all()
	serializer_class = IcCodeSerializer
	permission_class = (IsAuthenticated,)


class DiagnosesViewSet(viewsets.ModelViewSet):
	queryset = Diagnoses.objects.all()
	serializer_class = DiagnosesSerializer
	permission_class = (IsAuthenticated,)

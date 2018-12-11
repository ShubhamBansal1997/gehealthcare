from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import (
	PrescriptionSerializer
)
from ..models import (
	Prescription
)

class PrescriptionViewSet(viewsets.ModelViewSet):
	queryset = Prescription.objects.all()
	serializer_class = PrescriptionSerializer
	permission_class = (IsAuthenticated,)

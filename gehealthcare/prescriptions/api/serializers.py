from rest_framework import serializers
from ..models import Prescription


class PrescriptionSerializer(serializers.ModelSerializer):
	""""
	serializes the data of the basic IcCode api
	"""
	class Meta:
		model = Prescription
		fields = '__all__'
			
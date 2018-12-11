from rest_framework import serializers
from ..models import IcCode, Diagnoses


class IcCodeSerializer(serializers.ModelSerializer):
	""""
	serializes the data of the basic IcCode api
	"""
	class Meta:
		model = IcCode
		fields = '__all__'


class DiagnosesSerializer(serializers.ModelSerializer):
	"""
	serializes the data of the basic Diagnose api
	"""
	class Meta:
		model = Diagnoses
		fields = '__all__'
			
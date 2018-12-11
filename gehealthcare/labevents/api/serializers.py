from rest_framework import serializers
from ..models import Item, Labevent


class ItemSerializer(serializers.ModelSerializer):
	""""
	serializes the data of the basic IcCode api
	"""
	class Meta:
		model = Item
		fields = '__all__'


class LabeventSerializer(serializers.ModelSerializer):
	"""
	serializes the data of the basic Diagnose api
	"""
	class Meta:
		model = Labevent
		fields = '__all__'
			
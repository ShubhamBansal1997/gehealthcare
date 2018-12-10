from django.db import models
from gehealthcare.base.models import TimeStampedUUIDModel
from gehealthcare.users.models import User


class Item(TimeStampedUUIDModel):
	item_id = models.CharField(null=True, blank=True, max_length=250)
	item_name = models.TextField(null=True, blank=True)


class Labevent(TimeStampedUUIDModel):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	hadm_id = models.CharField(null=True, blank=True, max_length=100)
	item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)
	item_data_id = models.CharField(null=True, blank=True, max_length=250)
	charttime = models.DateTimeField(null=True, blank=True)
	value = models.CharField(null=True, blank=True, max_length=250)
	valueom = models.CharField(null=True, blank=True, max_length=250)
	flag = models.CharField(null=True, blank=True, max_length=50)
# Create your models here.

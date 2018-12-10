from django.db import models
from gehealthcare.base.models import TimeStampedUUIDModel
from gehealthcare.users.models import User
# Create your models here.


class IcCode(TimeStampedUUIDModel):
	ic_id = models.CharField(null=True, blank=True, max_length=250)
	ic_name = models.TextField(null=True, blank=True)


class Diagnoses(TimeStampedUUIDModel):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	hadm_id = models.CharField(null=True, blank=True, max_length=100)
	seq_num = models.IntegerField(null=True, blank=True)
	ic = models.ForeignKey(IcCode, null=True, on_delete=models.CASCADE)
	ic_data_id = models.CharField(null=True, blank=True, max_length=250)
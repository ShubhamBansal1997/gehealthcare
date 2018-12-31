from django.db import models
from gehealthcare.base.models import TimeStampedUUIDModel
from gehealthcare.users.models import User
# Create your models here.

class Prescription(TimeStampedUUIDModel):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	hadm_id = models.CharField(null=True, blank=True, max_length=100)
	startdate = models.DateField(null=True, blank=True)
	enddate = models.DateField(null=True, blank=True)
	drug = models.CharField(null=True, blank=True, max_length=250)
	drug_name = models.CharField(null=True, blank=True, max_length=250)
	webmd_link = models.TextField(null=True, blank=True)
	prod_strength = models.CharField(null=True, blank=True, max_length=200)
	dose_val = models.CharField(null=True, blank=True, max_length=20)
	dose_unit = models.CharField(null=True, blank=True, max_length=20)

	class Meta:
		verbose_name = 'Prescription'
		verbose_name_plural = 'Prescriptions'

	def __str__(self):
		return str(drug_name)
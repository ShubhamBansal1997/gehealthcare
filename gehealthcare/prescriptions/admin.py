from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.Prescription)
class PresscriptionAdmin(admin.ModelAdmin):
	list_display = ['user', 'hadm_id', 'startdate', 'enddate', 'drug', 'drug_name', 'prod_strength', 'dose_val', 'dose_unit']
	list_display_links = ['drug_name']
	search_fields = ('hadm_id', 'startdate', 'enddate', 'drug', 'drug_name', 'prod_strength', 'dose_val', 'dose_unit')
	ordering = ('startdate',)
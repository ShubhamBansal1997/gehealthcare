from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.IcCode)
class IcCodeAdmin(admin.ModelAdmin):
	list_display = ['ic_id', 'ic_name']
	list_display_links = ['ic_id']
	search_fields = ('ic_id', 'ic_name')
	ordering = ('ic_name',)


@admin.register(models.Diagnoses)
class DiagnosesAdmin(admin.ModelAdmin):
	list_display = ['user', 'hadm_id', 'ic', 'ic_data_id']
	list_display_links = ['user']
	list_filter = ['ic']
	search_fields = ('user', 'hadm_id', 'ic')
	ordering = ('user',)



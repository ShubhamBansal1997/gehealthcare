from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
	list_display = ['item_id', 'item_name']
	list_display_links = ['item_id']
	search_fields = ('item_id', 'item_name')
	ordering = ('item_id',)


@admin.register(models.Labevent)
class LabeventAdmin(admin.ModelAdmin):
	list_display = ['user', 'item', 'item_data_id', 'charttime', 'value', 'valueom', 'flag']
	list_display_links = ['item']
	list_filter = ['flag']
	search_fields = ('item', 'item_data_id', 'charttime', 'value', 'valueom', 'flag')
	ordering = ('charttime',)



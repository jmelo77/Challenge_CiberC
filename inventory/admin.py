from django.contrib import admin

from inventory.models import Inventory, UploadFile


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):

    list_display = ('serial_number', 'quantity', 'price')
    search_fields = ('serial_number',)
    list_filter = ('serial_number',)


@admin.register(UploadFile)
class UploadFileAdmin(admin.ModelAdmin):

    list_display = ('name', 'date', 'file_path', 'summary')
    search_fields = ('name', 'date',)
    list_filter = ('name', 'date',)

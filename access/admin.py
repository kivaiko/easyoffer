from django.contrib import admin
from .models import Access


@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'delete_date')
    search_fields = ('ip_address',)

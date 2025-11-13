from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_name', 'parent', 'order', 'get_url')
    list_filter = ('menu_name',)
    search_fields = ('name', 'menu_name', 'named_url', 'explicit_url')
    list_editable = ('order',)
    fields = ('name', 'menu_name', 'named_url', 'explicit_url', 'parent', 'order')

    def get_url(self, obj):
        return obj.get_url()
    get_url.short_description = 'URL'

admin.site.register(MenuItem, MenuItemAdmin)
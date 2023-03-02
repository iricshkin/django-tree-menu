from django.contrib import admin

from app.models import Item, Menu


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')
    search_fields = ('name',)
    list_filter = ('menu',)
    prepopulated_fields = {'slug': ('name',)}
    empty_value_display = '-пусто-'


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    empty_value_display = '-пусто-'


admin.site.register(Menu, MenuAdmin)
admin.site.register(Item, ItemAdmin)

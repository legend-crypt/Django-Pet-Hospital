from django.contrib import admin

from.models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'age','breed','sex','species']
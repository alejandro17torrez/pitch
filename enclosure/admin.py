from django.contrib import admin
from .models import Enclosure

# Register your models here.
@admin.register(Enclosure)
class EnclosureAdmin(admin.ModelAdmin):
    pass


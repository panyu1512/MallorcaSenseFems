from django.contrib import admin
from .models import Beach

# Register your models here.
@admin.register(Beach)
class MundoAdmin(admin.ModelAdmin):
    list_display = ('name','municipality')

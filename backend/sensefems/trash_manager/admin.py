from django.contrib import admin
from .models import Trash
# Register your models here.

@admin.register(Trash)
class TrashAdmin(admin.ModelAdmin):
    list_display = ('id', 'beach')
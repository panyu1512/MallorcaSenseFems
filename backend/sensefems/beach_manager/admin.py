from django.shortcuts import redirect, render
from django.contrib import admin
from django.urls import path
from django import forms
from .models import Beach
from .utils import import_beaches_csv

# Register your models here.
class CsvImportForm(forms.Form):
    csv_file = forms.FileField()
@admin.register(Beach)
class MundoAdmin(admin.ModelAdmin):
    change_list_template = "admin/changelist_beaches_template.html"
    list_display = ('name','municipality')

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-beaches-csv/', self.import_beaches_csv),
        ]
        return my_urls + urls

    def import_beaches_csv(self, request):
        if request.method == "POST":
            csv_file  = request.FILES["csv_file"]
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            import_beaches_csv(decoded_file)

            self.message_user(request, "Tu fichero CSV se ha subido correctamente.")
            return redirect("..")

        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_beaches_form.html", payload
        )
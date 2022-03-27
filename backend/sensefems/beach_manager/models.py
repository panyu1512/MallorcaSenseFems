from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Beach(models.Model):
    name = models.CharField(unique=True, max_length=255)
    municipality = models.CharField(max_length=255) 

    class Meta:
        verbose_name_plural = _("Beaches")
from django.db import models
from django.utils.translation import gettext_lazy as _
from beach_manager.models import Beach

# Create your models here.
class Trash(models.Model):
    beach = models.ForeignKey(Beach, on_delete=models.CASCADE, related_name="polluted_beach")
    municipality = models.ForeignKey(Beach, on_delete=models.CASCADE)
    type_waste = models.TextField()
    num_residues = models.IntegerField()
    pickup_date = models.DateTimeField()
    accepted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = _("Garbage Collection")
from django.db import models

# Create your models here.

class Candels(models.Model):

    csv_file = models.FileField(upload_to='documents/')
    time_frame = models.PositiveIntegerField()
    upload_at = models.DateTimeField(auto_now_add=True)
    json_file = models.FileField(upload_to='output/',blank=True)
from __future__ import unicode_literals
from django.db import models
# from django.utils import timezone

# from orca.scripts import self_voicing

# There is no actual data stored in this model. 
# It's only an example holding information about the file you uploaded


# Create your models here.
class UploadedFile(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='uploads/')    
    uploaded_at = models.DateTimeField(auto_now_add=True)

class apps(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    icon = models.CharField(max_length=64) # expect icon from respostyle.css

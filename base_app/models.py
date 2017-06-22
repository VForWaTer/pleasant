from django.db import models
from orca.scripts import self_voicing

# There is no actual data stored in this model. 
# It's only an example holding information about the file you uploaded


# Create your models here.
class UploadedFile(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='uploads/')    
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     name = models.CharField(max_length=255, blank=True)
#     type = models.CharField(max_length=128)
#     size = models.IntegerField()

#     def __unicode__(self):
#         return self.file.name
#     
# #     @models.permalink
# #     def get_absolute_url(self):
# #         return ('upload-new',)
# 
#     def save(self, *args, **kwargs):
#         self.slug = self.file.name
#         super(UploadedFile, self).save(*args, **kwargs)


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Project(models.Model):

    title = models.CharField()
    description = models.TextField()
    image = models.CloudinaryField('photos')
    project_url = models.URLField()

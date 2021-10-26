from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    image = CloudinaryField('photos')
    project_url = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='', null=True)

class Profile(models.Model):


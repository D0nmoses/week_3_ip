from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Project(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    image = CloudinaryField('photos')
    project_url = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True)

    
    @classmethod
    def search_projects(cls, name):
        return cls.objects.filter(title__icontains=name).all()
    
    def __str__(self):
        return self.title

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='avatars/')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(max_length=150, default="New Here")

    def __str__(self):
        return self.username

# Create Profile when creating a User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save Profile when saving a User
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


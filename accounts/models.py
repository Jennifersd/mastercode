from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    EXPERIENCE_CHOICES = (
        ('Less than 1 yr', 'Less than 1 yr'),
        ('1 to 3 yr', '1 to 3 yr' ),
        ('More than 3 yr', 'More than 3 yr'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location =  models.CharField(max_length=250, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    career =  models.CharField(max_length=250, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **Kwargs):
    if created:
        Profile.objects.created(user=instance)
        
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **Kwargs):  
    instance.profile.save()      

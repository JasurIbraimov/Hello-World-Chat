from django.db import models

# Create your models here.

class UserProfile(models.Model):
	email = models.CharField(max_length=150)
	username = models.CharField(max_length=150)
	userphoto = models.ImageField(upload_to="images/profile", null=True, blank=True)
	

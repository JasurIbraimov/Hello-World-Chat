from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
from datetime import datetime, date 


class ChatMessage(models.Model):
	message = models.CharField(max_length=150)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	send_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.message + ' | ' + str(self.author)


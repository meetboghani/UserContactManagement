from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

class usersave(models.Model):

    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    middle = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    email = models.EmailField()
    phoneno = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=100)

class Contact(models.Model):
    client_name = models.CharField(max_length=200)
    client_email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    client_message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

class SaveContact(models.Model):
    user_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=1000)

    def __str__(self):
          return self.full_name 
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    username = models.SlugField(default="", null=False, db_index=True, blank=True)  # forced by django admin problems :(
    password = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, unique=True)
    reputation = models.DecimalField(max_digits=7, decimal_places=1, default=1.0)
    phoneNum = PhoneNumberField(null=False, unique=True, default='')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "password"]

    def save(self, *args, **kwargs):
        self.username = slugify(f'{self.first_name} {self.last_name}')
        super().save(*args, **kwargs)

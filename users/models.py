from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    username = models.CharField(default="", null=False, db_index=True, blank=True,
                                unique=True)
    password = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, unique=True)
    reputation = models.DecimalField(max_digits=7, decimal_places=1, default=1.0)
    phoneNum = PhoneNumberField(null=False, unique=True, default='')
    profile = models.ImageField(upload_to="profile/", null=True, blank=True,
                                default="https://www.seekpng.com/png/detail/413-4139803_unknown-profile-profile-picture-unknown.png")
    description = models.TextField(blank=True, null=True, default="No Description Provided(He/She is Gay)")
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name", "password"]

    def __str__(self):
        return f"{self.username}:{self.first_name} {self.last_name}"

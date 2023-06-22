from django.db import models
from users.models import User
from django.utils import timezone


# Create your models here.
class Code(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Code_Author")
    short_description = models.CharField(max_length=100, null=False, default="No Description Provided")
    code_text = models.TextField(blank=True, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    TYPE_CHOICES = [
        ("TXT", "TextFile"),
        ("PY", "Python"),
        ("JS", "Javascript"),
        ("C", "C"),
        ("CPP", "C++"),
        ("CS", "Csharp"),
        ("JV", "Java"),
    ]
    type = models.CharField(max_length=3, choices=TYPE_CHOICES, default="TXT")


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Question_Author", null=True)
    short_description = models.CharField(max_length=100, null=False, default="No Description Provided")
    description = models.TextField(null=False, default="No Description Provided")
    code = models.ManyToManyField(Code)
    created_at = models.DateTimeField(default=timezone.now)


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Answer_Author")
    short_description = models.CharField(max_length=100, null=False, default="No Description Provided")
    description = models.TextField(null=False, default="No Description Provided")
    code = models.ForeignKey(Code, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)

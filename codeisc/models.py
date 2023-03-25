from django.db import models
from users.models import User


# Create your models here.
class Code(models.Model):
    author = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="Code_Author")
    description = models.CharField(max_length=255, null=False, default="No Description Provided")
    code_text = models.TextField(blank=True, null=False)
    type = models.CharField(max_length=3, choices=[
        ("TXT", "TextFile"),
        ("PY", "Python"),
        ("PY", "Python"),
        ("JS", "Javascript"),
        ("TS", "Typescript"),
        ("C", "C"),
        ("CPP", "C++"),
        ("CS", "Csharp"),
        ("JV", "Java"),
    ], default="TXT")
    score = models.IntegerField(default=0, null=False)


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="Answer_Author")
    text = models.TextField(null=False, blank=True)
    code = models.ManyToManyField(Code)
    score = models.IntegerField(default=0, null=False)


class Question(models.Model):
    pass

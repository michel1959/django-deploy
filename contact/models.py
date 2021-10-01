from django.db import models
from tinymce import models as tinymce_models


class Contact(models.Model):
    name = models.TextField()
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

# Create your models here.

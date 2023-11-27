from django.db import models

# Create your models here.

class Words(models.Model):
    word = models.CharField(max_length=200)
    joke = models.CharField()

    def __str__(self):
        return self.word

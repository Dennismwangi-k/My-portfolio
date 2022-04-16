from django.db import models

# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/gallary/')
    description = models.CharField(max_length=200)
    technology = models.CharField(max_length=20)
    link = models.CharField(max_length=200, default='', blank=True, null=True)

    def __str__(self):
        return self.title

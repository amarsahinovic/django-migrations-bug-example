from django.db import models
from galleries.models import Gallery

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    gallery = models.ForeignKey(Gallery, related_name='articles')

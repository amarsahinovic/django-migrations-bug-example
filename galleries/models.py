from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=255)


class GalleryItem(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='gallery_items')
    image = models.CharField(max_length=255)

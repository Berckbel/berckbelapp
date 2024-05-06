from django.db import models

# Create your models here.
class UrlShort(models.Model):
    original_url = models.URLField(max_length=255, unique=True, null=False, blank=False)
    url_hash = models.TextField(max_length=255, unique=True, null=False, blank=False)
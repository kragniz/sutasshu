from __future__ import unicode_literals

from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200)
    added_date = models.DateTimeField('date added',
                                      auto_now_add=True)
    image = models.ImageField()

# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return u'%s' % self.name

from django.contrib.auth.models import User
from django.db import models

from pymongo import Connection

class MongoConnection(models.Model):
    user = models.ForeignKey(User)

    name = models.CharField(max_length=255)

    host = models.CharField(max_length=255)
    port = models.IntegerField(default=27017)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    # ssh


    def __unicode__(self):
        return self.name

    def get_connection(self):
        return Connection(self.host, int(self.port), username=self.username, password=self.password)

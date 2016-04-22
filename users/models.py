from __future__ import unicode_literals

from django.db import models

class AppUser(models.Model):
    """Model which extends the inbuild User model"""
    fb_auth = models.CharField(max_length=1024)
    google_auth = models.CharField(max_length=1024)
    user = models.OneToOneField(to='auth.User', related_name='app_user')

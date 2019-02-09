from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from s3direct.fields import S3DirectField

class Profile(models.Model):
    # def image_tag(self):
    #    return u'<img src="%s" />' % {{ self.avatar.url }}
    # image_tag.short_description = 'Image'
    # image_tag.allow_tags = True

    avatar = S3DirectField(dest='profiles')
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    twitter_username = models.CharField(max_length=255, null=True, blank=True)
    instagram_username = models.CharField(max_length=255, null=True, blank=True)
    linkedin_username = models.CharField(max_length=255, null=True, blank=True)

class Project(models.Model):
    TYPE_CHOICES = (
        (1, 'Development'),
        (2, 'Design'),
        (3, 'Social Media & Marketing'),
        (4, 'Visual Media'),
    )

    name = models.CharField(max_length=255)
    type = models.IntegerField(
        choices=TYPE_CHOICES,
        default=1,
    )
    client = models.CharField(max_length=255)
    date_completed = models.DateField(default=datetime.now)
    description = models.TextField(null=True, blank=True)
    tesimonial = models.TextField(null=True, blank=True)
    main_image = S3DirectField(dest='projects', null=True)
    def __str__(self):
        return self.name


class Image(models.Model):
    image = S3DirectField(dest='projects', null=True)
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = S3DirectField(dest='services', null=True, blank=True)
    enabled = models.BooleanField(default=False)
    parent = models.BooleanField(default=False)
    parent_service = models.ForeignKey('Service', on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'parent': True})
    def __str__(self):
        return self.name

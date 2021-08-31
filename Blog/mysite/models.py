from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    name = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True, null=True)
    subjects = models.ManyToManyField('Subject', related_name='blogs', null=True, blank=True)
    sections = models.ForeignKey(to='Section', null=True, blank=True, related_name='blog', on_delete=models.CASCADE)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateField(auto_now_add=True, null=True)
    color = models.ForeignKey('SubjectColor', null=True, blank=True, related_name='subjects', on_delete=models.CASCADE)


class SubjectColor(models.Model):
    color_name = models.CharField(max_length=100, null=True, blank=True)
    hex_code = models.CharField(max_length=20, null=True, blank=True)


class Section(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=3000, blank=True)

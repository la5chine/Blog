from django.contrib.auth.models import User
from rest_framework import serializers

from Blog.mysite.models import Blog, Subject, SubjectColor, Section


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ['author', 'name', 'publish_date', 'subjects', 'sections']


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'create_date', 'color']


class SubjectColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubjectColor
        fields = '__all__'


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

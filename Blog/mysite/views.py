from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from Blog.mysite.models import Blog, Subject, SubjectColor, Section
from Blog.mysite.serializers import UserSerializer, BlogSerializer, SubjectSerializer, SubjectColorSerializer, \
    SectionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class BlogSerializerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Blog to be viewed or edited.
    """
    queryset = Blog.objects.all().prefetch_related('subjects')
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubjectSerializerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Subject to be viewed or edited.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubjectColorSerializerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SubjectColor to be viewed or edited.
    """
    queryset = SubjectColor.objects.all()
    serializer_class = SubjectColorSerializer
    permission_classes = [permissions.IsAuthenticated]


class SectionSerializerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SubjectColor to be viewed or edited.
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [permissions.IsAuthenticated]

from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import permissions


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
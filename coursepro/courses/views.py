from rest_framework import viewsets
from .models import Lesson, Course, Teacher
from . import serializers
from rest_framework import permissions
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404


class CourseListView(ListView):
    template_name = 'course_list.html'
    model = Course


class TeacherListView(ListView):
    model = Teacher


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer


class LessonListView(ListView):
    template_name = 'lesson_list.html'
    model = Lesson

    def get_queryset(self):
        self.course = get_object_or_404(Course, id=self.kwargs['pk'])
        return Lesson.objects.filter(course=self.course)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.course
        return context


class LessonDetailView(DetailView):
    model = Lesson

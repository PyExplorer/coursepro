from rest_framework import viewsets
from .models import Lesson, Course, Teacher
from . import serializers
from rest_framework import permissions
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.http import HttpResponseRedirect

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


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
        else:
            return redirect('/')
    else:
        form = RegistrationForm()
        args = {'form': form}
    return render(request, 'registration/registration_form.html', args)


def home(request):
    return render(request, 'home.html')
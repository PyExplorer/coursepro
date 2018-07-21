from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rest_framework import permissions
from rest_framework import viewsets

from . import serializers
from .forms import RegistrationForm, LoginForm
from .models import Lesson, Course, Teacher


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


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')
        else:
            return redirect('/')
    else:
        form = RegistrationForm()
        args = {'form': form}
    return render(request, 'accounts/signup.html', args)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
        else:
            return redirect('/account/logout')
    else:
        form = LoginForm()
        args = {'form': form}
    return render(request, 'accounts/login.html', args)


def home(request):
    return render(request, 'home.html')


def login_redirect(request):
    return redirect('/account/login/')


def home_redirect(request):
    return redirect('/home/')

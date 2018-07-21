
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from courses import views as course_views
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'courses', course_views.CourseViewSet)

urlpatterns = [

    path('courses/', course_views.CourseListView.as_view(),
         name='courses'),
    path('courses/<int:pk>/', course_views.LessonListView.as_view(),
         name='lessons_list'),
    path('courses/lessons/<int:pk>/', course_views.LessonDetailView.as_view(),
         name='lesson_details'),

    path('admin/', admin.site.urls),

    path('account/', include('courses.account_urls')),

    path(r'home/', course_views.home, name="home"),
    path(r'', course_views.home_redirect, name="home_redirect"),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

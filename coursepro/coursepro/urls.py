
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from courses import views as course_views
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'courses', course_views.CourseViewSet)

urlpatterns = [

    path('courses/', course_views.CourseListView.as_view()),
    path('courses/<int:pk>/', course_views.LessonListView.as_view(),
         name='lessons_list'),
    path('courses/lessons/<int:pk>/', course_views.LessonDetailView.as_view(),
         name='lesson_details'),


    path('admin/', admin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls')),

    re_path(r'^accounts/', include('django.contrib.auth.urls')),

    path(r'', include(router.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
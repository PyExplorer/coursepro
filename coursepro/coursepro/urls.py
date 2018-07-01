
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from courses import views as course_views


router = routers.DefaultRouter()
router.register(r'courses', course_views.CourseViewSet)

urlpatterns = [
    path('a dmin/', admin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    path(r'', include(router.urls)),
]

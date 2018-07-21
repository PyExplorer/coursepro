from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class StrMixin(object):
    title = ''

    def __str__(self):
        return self.title


class Course(StrMixin, models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    curator = models.ForeignKey('Teacher', on_delete='CASCADE', default=0)


class Lesson(StrMixin, models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    date = models.DateField(null=True)
    course = models.ForeignKey('Course', on_delete='CASCADE')
    teacher = models.ForeignKey('Teacher', on_delete='CASCADE', default=0)


class Teacher(StrMixin, models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=True)
    description = models.CharField(max_length=512, default='')
    first_name = models.CharField(max_length=512, default='')
    second_name = models.CharField(max_length=512, default='')
    email = models.EmailField()


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)

# зарегистрироваться
# залогиниться
# посмотреть список курсов
# зайти в курс
# посмотреть описание
# посмотреть список занятий

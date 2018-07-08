from django.db import models


class StrMixin(object):
    title = ''

    def __str__(self):
        return self.title


class Course(StrMixin, models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    curator = models.ForeignKey('Teacher', on_delete='CASCADE', default=0)
    price = models.IntegerField()


class Lesson(StrMixin, models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    date = models.DateField(null=True)
    course = models.ForeignKey('Course', on_delete='CASCADE')
    teacher = models.ForeignKey('Teacher', on_delete='CASCADE', default=0)


class Teacher(StrMixin, models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()



        # зарегистрироваться
    # залогиниться
    # посмотреть список курсов
    # зайти в курс
    # посмотреть описание
    # посмотреть список занятий


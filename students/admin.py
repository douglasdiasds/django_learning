from django.contrib import admin

# Register your models here.
from students.models import Student
from courses.models import Course
from enrollments.models import Enrollment

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
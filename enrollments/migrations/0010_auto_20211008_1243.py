# Generated by Django 2.2 on 2021-10-08 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enrollments', '0009_auto_20211007_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='courses', to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='date_enroll',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='students', to='students.Student'),
        ),
    ]
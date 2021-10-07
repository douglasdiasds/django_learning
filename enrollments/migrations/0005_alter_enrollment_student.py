# Generated by Django 3.2.7 on 2021-10-07 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_nick_name'),
        ('enrollments', '0004_enrollment_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='enrollments', to='students.student'),
        ),
    ]

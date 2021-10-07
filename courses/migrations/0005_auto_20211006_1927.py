# Generated by Django 3.2.7 on 2021-10-06 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_holder_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(default='Description', max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.IntegerField(max_length=10),
        ),
    ]
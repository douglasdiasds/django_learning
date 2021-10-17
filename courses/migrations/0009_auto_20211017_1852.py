# Generated by Django 3.2.7 on 2021-10-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_coursecontent_mandatory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursecontent',
            name='mandatory',
        ),
        migrations.AddField(
            model_name='course',
            name='mandatory',
            field=models.BooleanField(blank=True, null=True, verbose_name='Mandatory'),
        ),
    ]

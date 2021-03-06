# Generated by Django 2.2 on 2021-10-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20211008_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='content_type',
            field=models.CharField(choices=[('V', 'Video'), ('P', 'Pdf')], default=0, max_length=1, verbose_name='Content Type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='duration',
            field=models.IntegerField(default=0, verbose_name='Duration'),
        ),
        migrations.AlterField(
            model_name='content',
            name='description',
            field=models.CharField(default='Description', max_length=200, verbose_name='Description'),
        ),
    ]

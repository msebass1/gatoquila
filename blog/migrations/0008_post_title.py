# Generated by Django 3.0.3 on 2020-03-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200311_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]

# Generated by Django 3.0.3 on 2020-03-12 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200312_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gato',
            name='foto',
            field=models.CharField(max_length=200),
        ),
    ]

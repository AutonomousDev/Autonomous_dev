# Generated by Django 3.2.9 on 2021-12-19 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20211218_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='project_pics'),
        ),
    ]

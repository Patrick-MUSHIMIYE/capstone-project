# Generated by Django 4.2.9 on 2024-01-19 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostfound_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_image',
            name='tel',
            field=models.CharField(max_length=254),
        ),
    ]

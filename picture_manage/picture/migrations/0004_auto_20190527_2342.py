# Generated by Django 2.0.7 on 2019-05-27 15:42

from django.db import migrations, models
import picture.models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0003_auto_20190527_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(upload_to=picture.models.Picture.user_directory_path),
        ),
    ]

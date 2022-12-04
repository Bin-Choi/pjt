# Generated by Django 3.2.13 on 2022-11-22 14:38

import accounts.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20221122_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='backdrop_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='backdrop/default.jpg', upload_to=accounts.models.backdrop_image_path),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='profile/default.png', upload_to=accounts.models.profile_image_path),
        ),
    ]

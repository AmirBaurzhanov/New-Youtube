# Generated by Django 3.2.4 on 2021-12-18 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='logo',
            field=models.ImageField(null=True, upload_to='video_logo/'),
        ),
    ]
# Generated by Django 2.0.4 on 2018-04-16 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='user.jpg', upload_to='profile_image'),
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-17 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SocialX', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile_pic',
            old_name='name',
            new_name='username',
        ),
    ]
# Generated by Django 4.2 on 2023-06-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, default='https://www.seekpng.com/png/detail/413-4139803_unknown-profile-profile-picture-unknown.png', null=True, upload_to='profile/'),
        ),
    ]
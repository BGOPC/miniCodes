# Generated by Django 4.2.3 on 2023-07-15 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeisc', '0018_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='tags',
            field=models.ManyToManyField(to='codeisc.tag'),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='codeisc.tag'),
        ),
    ]

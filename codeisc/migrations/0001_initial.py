# Generated by Django 4.1.7 on 2023-03-25 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='No Description Provided', max_length=255)),
                ('code_text', models.TextField(blank=True)),
                ('type', models.CharField(choices=[('TXT', 'TextFile'), ('PY', 'Python'), ('PY', 'Python'), ('JS', 'Javascript'), ('TS', 'Typescript'), ('C', 'C'), ('CPP', 'C++'), ('CS', 'Csharp'), ('JV', 'Java')], default='TXT', max_length=3)),
                ('score', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='Code_Author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('score', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='Answer_Author', to=settings.AUTH_USER_MODEL)),
                ('code', models.ManyToManyField(to='codeisc.code')),
            ],
        ),
    ]

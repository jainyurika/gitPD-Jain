# Generated by Django 3.1.7 on 2021-04-18 00:13

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
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('description', models.TextField(max_length=5000, verbose_name='Description')),
                ('upvotecount', models.IntegerField(default=0, verbose_name='Upvote Count')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Post Created On')),
                ('slug', models.SlugField(unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=5000, null=True, verbose_name='Description')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Comment Created On')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discussionforum.post')),
            ],
        ),
    ]

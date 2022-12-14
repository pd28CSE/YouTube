# Generated by Django 4.1.1 on 2022-10-28 15:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('channelanalytics', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Play List Name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlist', to='channelanalytics.channel', verbose_name='Channel Name')),
            ],
            options={
                'verbose_name_plural': 'Play List',
                'unique_together': {('title', 'channel')},
            },
        ),
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenttitle', models.CharField(max_length=300)),
                ('file', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])], verbose_name='Your Video Content')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('playlisttitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videocontents', to='contents.playlist', verbose_name='Select Play List Name')),
            ],
            options={
                'verbose_name': 'Video Content',
                'verbose_name_plural': 'Video Contents',
            },
        ),
        migrations.CreateModel(
            name='VideoHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('user', models.ManyToManyField(related_name='history', to=settings.AUTH_USER_MODEL, verbose_name='User Name')),
                ('video', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='contents.videocontent', verbose_name='Watch Video')),
            ],
            options={
                'verbose_name': 'Video History',
                'verbose_name_plural': 'Video History',
            },
        ),
        migrations.CreateModel(
            name='UserReact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('react', models.CharField(choices=[('LO', 'Love'), ('AN', 'Angry'), ('LI', 'Like'), ('DI', 'Dislike'), ('NO', 'NO React')], max_length=2)),
                ('content', models.ManyToManyField(related_name='react', to='contents.videocontent', verbose_name='Select Content')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactuser', to=settings.AUTH_USER_MODEL, verbose_name='Liked User')),
            ],
            options={
                'verbose_name_plural': 'User React',
            },
        ),
    ]

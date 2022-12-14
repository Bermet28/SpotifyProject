# Generated by Django 4.1.2 on 2022-10-20 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music', '0002_music_creator_music_time_length_album'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='music.music')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='music.music')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('music', 'owner')},
            },
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='music.music')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('music', 'owner')},
            },
        ),
    ]

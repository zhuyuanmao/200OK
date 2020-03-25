# Generated by Django 2.1.5 on 2020-03-24 01:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_id', models.CharField(max_length=100)),
                ('friend_displayName', models.CharField(max_length=20)),
                ('friend_host', models.CharField(max_length=100)),
                ('friend_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='date posted')),
                ('author_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_from', to='friendship.Friend')),
                ('author_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_to', to='friendship.Friend')),
            ],
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_a', to='friendship.Friend')),
                ('author_b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_b', to='friendship.Friend')),
            ],
        ),
    ]

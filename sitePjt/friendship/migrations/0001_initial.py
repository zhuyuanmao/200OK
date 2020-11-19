# Generated by Django 2.2.2 on 2020-11-19 07:41

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
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('displayName', models.CharField(max_length=30)),
                ('host', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
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
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='date posted')),
                ('author_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_from', to='friendship.Friend')),
                ('author_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_to', to='friendship.Friend')),
            ],
        ),
    ]

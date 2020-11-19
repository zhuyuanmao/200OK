# Generated by Django 2.2.2 on 2020-11-19 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('contentType', models.CharField(choices=[('text/markdown', 'Markdown'), ('application/base64', 'Application'), ('text/plain', 'Plain text'), ('image/jpeg;base64', 'Image/jpeg'), ('image/png;base64', 'Image/png')], default='text/plain', max_length=20)),
                ('origin', models.CharField(default='', editable=False, max_length=200)),
                ('source', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField()),
                ('categories', models.CharField(blank=True, max_length=200)),
                ('unlisted', models.BooleanField(choices=[(False, 'False'), (True, 'True')], default=False)),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='date posted')),
                ('visibility', models.CharField(choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Prviate to self'), ('FRIENDS', 'Private to friends'), ('FOAF', 'Private to friends of friends'), ('SERVERONLY', 'Private to local friends')], default='PUBLIC', max_length=10)),
                ('visibleTo', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('contentType', models.CharField(choices=[('text/markdown', 'Markdown'), ('text/plain', 'Plain Text')], default='text/plain', max_length=20)),
                ('comment', models.CharField(max_length=288)),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='date posted')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posting.Post')),
            ],
        ),
    ]

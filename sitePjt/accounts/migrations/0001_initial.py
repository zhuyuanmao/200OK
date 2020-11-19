# Generated by Django 2.2.2 on 2020-11-19 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email address')),
                ('id', models.CharField(default='448415db-a89f-4935-ae88-f20b26a6194f', editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('displayName', models.CharField(max_length=30)),
                ('lastName', models.CharField(blank=True, max_length=30)),
                ('firstName', models.CharField(blank=True, max_length=30)),
                ('host', models.CharField(default='https://yuanmao-demo.herokuapp.com/', max_length=100)),
                ('url', models.CharField(default='', max_length=100)),
                ('avatar', models.ImageField(blank=True, default='avatar/default-avatar.png', null=True, upload_to='avatar/')),
                ('github', models.URLField(default='', max_length=100, null=True)),
                ('bio', models.CharField(blank=True, default='This guy is too lazy to write a bio...', max_length=200, null=True)),
                ('date_joined', models.DateField(auto_now=True, verbose_name='date joined')),
                ('last_login', models.DateField(auto_now=True, verbose_name='last login')),
                ('active', models.BooleanField(default=True)),
                ('activated', models.BooleanField(default=True)),
                ('node', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('share', models.BooleanField(default=False)),
                ('share_image', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServerNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_username', models.CharField(max_length=100)),
                ('server_password', models.CharField(max_length=100)),
                ('token', models.CharField(blank=True, max_length=200)),
                ('host_url', models.CharField(max_length=200)),
            ],
        ),
    ]

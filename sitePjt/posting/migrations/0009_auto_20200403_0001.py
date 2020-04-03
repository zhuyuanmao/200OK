# Generated by Django 2.2.2 on 2020-04-03 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0008_auto_20200402_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='contentType',
            field=models.CharField(choices=[('text/plain', 'Plain Text'), ('text/markdown', 'Markdown')], default='text/plain', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='contentType',
            field=models.CharField(choices=[('text/plain', 'Plain text'), ('text/markdown', 'Markdown'), ('application/base64', 'Application'), ('image/png;base64', 'Image/png'), ('image/jpeg;base64', 'Image/jpeg')], default='text/plain', max_length=20),
        ),
    ]

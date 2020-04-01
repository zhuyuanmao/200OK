# Generated by Django 2.2.2 on 2020-04-01 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0004_auto_20200401_0131'),
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
            field=models.CharField(choices=[('text/plain', 'Plain text'), ('image/jpeg;base64', 'Image/jpeg'), ('image/png;base64', 'Image/png'), ('text/markdown', 'Markdown'), ('application/base64', 'Application')], default='text/plain', max_length=20),
        ),
    ]
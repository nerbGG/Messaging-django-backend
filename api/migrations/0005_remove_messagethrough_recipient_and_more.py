# Generated by Django 4.0.5 on 2022-06-06 21:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_remove_messagethrough_recipient_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagethrough',
            name='recipient',
        ),
        migrations.AddField(
            model_name='messagethrough',
            name='recipient',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

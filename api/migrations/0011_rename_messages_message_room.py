# Generated by Django 4.0.5 on 2022-06-07 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_room_messages_message_messages_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='messages',
            new_name='room',
        ),
    ]

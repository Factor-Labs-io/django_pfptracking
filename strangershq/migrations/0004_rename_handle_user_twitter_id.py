# Generated by Django 4.1.1 on 2023-05-21 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strangershq', '0003_remove_user_id_alter_user_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='handle',
            new_name='twitter_id',
        ),
    ]
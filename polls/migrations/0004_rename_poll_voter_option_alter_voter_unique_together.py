# Generated by Django 4.1.4 on 2022-12-30 09:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0003_alter_voter_poll'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voter',
            old_name='poll',
            new_name='option',
        ),
        migrations.AlterUniqueTogether(
            name='voter',
            unique_together={('option', 'user')},
        ),
    ]

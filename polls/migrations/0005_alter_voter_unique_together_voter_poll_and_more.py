# Generated by Django 4.1.4 on 2022-12-30 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_rename_poll_voter_option_alter_voter_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='voter',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='voter',
            name='poll',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.question'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='voter',
            name='option',
        ),
    ]
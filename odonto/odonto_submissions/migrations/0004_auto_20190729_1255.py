# Generated by Django 2.0.13 on 2019-07-29 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odonto_submissions', '0003_auto_20190729_1255'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bcds1message',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='bcds1message',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='bcds1message',
            name='user',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='message',
        ),
        migrations.DeleteModel(
            name='BCDS1Message',
        ),
    ]

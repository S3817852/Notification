# Generated by Django 3.2 on 2021-04-30 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_alter_notification_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_commented',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('message', 'Message'), ('application', 'Application'), ('comment', 'Comment')], max_length=20),
        ),
    ]

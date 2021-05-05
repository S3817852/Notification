# Generated by Django 3.2 on 2021-05-05 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_remove_application_experience'),
        ('userprofile', '0007_conversationmessage_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationmessage',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversationmessages', to='job.application'),
        ),
    ]
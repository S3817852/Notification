# Generated by Django 3.2 on 2021-04-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0004_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

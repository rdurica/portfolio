# Generated by Django 4.1 on 2022-08-27 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
# Generated by Django 4.0.4 on 2022-04-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.TextField(max_length=800),
        ),
    ]
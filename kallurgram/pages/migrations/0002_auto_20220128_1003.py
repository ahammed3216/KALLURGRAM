# Generated by Django 2.2.20 on 2022-01-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
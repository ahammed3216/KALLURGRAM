# Generated by Django 2.2.20 on 2022-01-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20220126_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
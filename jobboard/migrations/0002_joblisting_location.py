# Generated by Django 4.2.6 on 2024-01-04 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

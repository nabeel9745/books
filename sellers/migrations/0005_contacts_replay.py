# Generated by Django 4.1.2 on 2022-10-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0004_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='replay',
            field=models.CharField(default='', max_length=100),
        ),
    ]

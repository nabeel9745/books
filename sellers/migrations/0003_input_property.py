# Generated by Django 4.1 on 2022-09-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0002_alter_registration_address_alter_registration_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='input_property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=50)),
                ('p_address', models.CharField(max_length=50)),
                ('p_landmark', models.CharField(max_length=50)),
                ('P_city', models.CharField(max_length=50)),
                ('p_state', models.CharField(max_length=10)),
                ('p_pincode', models.BigIntegerField()),
            ],
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-25 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudtest', '0003_alter_big_form_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_name', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='big_form',
            name='approved',
            field=models.CharField(default='not approved', max_length=100),
        ),
    ]

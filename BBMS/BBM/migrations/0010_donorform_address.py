# Generated by Django 3.1.1 on 2020-10-03 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBM', '0009_remove_donorform_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='donorform',
            name='address',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]

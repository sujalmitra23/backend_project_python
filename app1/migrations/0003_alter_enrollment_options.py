# Generated by Django 5.1.1 on 2024-10-23 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_enrollment_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enrollment',
            options={'ordering': ['enrollment_date']},
        ),
    ]

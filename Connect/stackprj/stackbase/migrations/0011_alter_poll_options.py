# Generated by Django 5.0.4 on 2024-05-26 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stackbase', '0010_poll_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poll',
            options={'ordering': ['-date_created']},
        ),
    ]

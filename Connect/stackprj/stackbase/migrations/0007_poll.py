# Generated by Django 5.0.4 on 2024-05-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackbase', '0006_question_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_one', models.CharField(max_length=30)),
                ('option_two', models.CharField(max_length=30)),
                ('option_three', models.CharField(max_length=30)),
                ('option_one_count', models.IntegerField(default=0)),
                ('option_two_count', models.IntegerField(default=0)),
                ('option_three_count', models.IntegerField(default=0)),
            ],
        ),
    ]

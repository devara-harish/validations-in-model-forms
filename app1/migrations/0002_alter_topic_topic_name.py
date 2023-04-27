# Generated by Django 4.1.7 on 2023-04-27 04:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, validators=[django.core.validators.MaxLengthValidator(3)]),
        ),
    ]

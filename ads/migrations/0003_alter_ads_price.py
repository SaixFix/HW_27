# Generated by Django 4.1.5 on 2023-02-01 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='price',
            field=models.IntegerField(),
        ),
    ]

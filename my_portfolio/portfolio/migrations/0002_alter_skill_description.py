# Generated by Django 5.0.7 on 2024-07-20 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(null=True),
        ),
    ]

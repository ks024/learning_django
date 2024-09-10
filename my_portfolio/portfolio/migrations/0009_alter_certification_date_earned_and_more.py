# Generated by Django 5.0.7 on 2024-07-26 02:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_certification_date_earned_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='date_earned',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='parent_certification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_certification_set', to='portfolio.certification'),
        ),
        migrations.AlterField(
            model_name='certification',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

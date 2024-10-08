# Generated by Django 5.0.7 on 2024-07-24 15:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_certification_authority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='parent_certification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_certification_set', to='portfolio.certification'),
        ),
        migrations.AlterField(
            model_name='certification',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

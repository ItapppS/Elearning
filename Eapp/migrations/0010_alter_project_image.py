# Generated by Django 5.1.4 on 2025-03-20 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eapp', '0009_merge_20250320_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='project_images/'),
        ),
    ]

# Generated by Django 4.0.8 on 2024-08-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_upload_file_alter_uploadvideo_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('Bachelor', 'Bachelor Degree'), ('Master', 'Master Degree')], max_length=25, null=True),
        ),
    ]

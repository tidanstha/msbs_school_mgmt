# Generated by Django 4.0.8 on 2024-08-12 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_alter_course_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('Bachelors', 'Bachelor Degree'), ('Master', 'Master Degree')], max_length=25, null=True),
        ),
    ]

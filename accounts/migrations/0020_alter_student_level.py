# Generated by Django 4.0.8 on 2024-08-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('Bachelor', 'Bachelor Degree'), ('Master', 'Master Degree')], max_length=25, null=True),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
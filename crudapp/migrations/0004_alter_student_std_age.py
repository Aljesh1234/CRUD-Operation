# Generated by Django 4.2.5 on 2024-06-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='std_age',
            field=models.IntegerField(),
        ),
    ]
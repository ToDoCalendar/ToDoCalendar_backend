# Generated by Django 4.0.5 on 2022-06-28 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_task_complited_alter_task_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complited',
            new_name='completed',
        ),
    ]

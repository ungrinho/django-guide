# Generated by Django 4.2.11 on 2024-05-03 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_todo_important'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-30 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0004_task_add_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='pro_add',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]

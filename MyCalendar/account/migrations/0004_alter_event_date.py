# Generated by Django 4.0.4 on 2022-04-30 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(verbose_name='date'),
        ),
    ]

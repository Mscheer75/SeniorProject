# Generated by Django 3.0.9 on 2020-11-09 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustApp', '0008_workorder_pickedup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='PickedUp',
            field=models.BooleanField(),
        ),
    ]

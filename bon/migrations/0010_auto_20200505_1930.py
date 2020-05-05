# Generated by Django 2.2.5 on 2020-05-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bon', '0009_auto_20200502_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Total_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Scheduled', 'Scheduled'), ('delayed', 'delayed'), ('Deliveried', 'Deliveried'), ('Shipped', 'Shipped'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Active', max_length=10),
        ),
    ]
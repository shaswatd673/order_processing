# Generated by Django 2.2.5 on 2020-05-02 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bon', '0008_auto_20200426_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Scheduled', 'Scheduled'), ('delayed', 'delayed'), ('Deliveried', 'Deliveried'), ('Shipped', 'Shipped')], default='Active', max_length=10),
        ),
        migrations.AddField(
            model_name='orders',
            name='status_description',
            field=models.TextField(default='None'),
        ),
    ]

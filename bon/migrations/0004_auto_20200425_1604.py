# Generated by Django 2.2.5 on 2020-04-25 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bon', '0003_auto_20200425_0956'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='part_list',
            unique_together={('designID', 'PartID')},
        ),
    ]

# Generated by Django 2.1.8 on 2019-04-01 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20190401_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventdetail',
            old_name='image',
            new_name='photo',
        ),
    ]

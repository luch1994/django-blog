# Generated by Django 3.0.2 on 2020-02-18 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20200218_0941'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Comments',
        ),
    ]
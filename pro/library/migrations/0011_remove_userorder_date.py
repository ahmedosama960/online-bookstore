# Generated by Django 3.2.3 on 2021-06-04 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_alter_userorder_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userorder',
            name='date',
        ),
    ]
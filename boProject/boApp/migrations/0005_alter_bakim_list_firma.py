# Generated by Django 3.2.13 on 2022-05-13 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boApp', '0004_alter_bakim_list_durum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakim_list',
            name='firma',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

# Generated by Django 3.2.13 on 2022-04-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boApp', '0002_auto_20220423_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakim_list',
            name='ilkfoto',
            field=models.ImageField(blank=True, null=True, upload_to='bakimOnarim/ilkfoto/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='bakim_list',
            name='sonFoto',
            field=models.ImageField(blank=True, null=True, upload_to='bakimOnarim/sonFoto/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='bakim_list',
            name='tutanak',
            field=models.ImageField(blank=True, null=True, upload_to='bakimOnarim/tutanak/%Y/%m/%d/'),
        ),
    ]

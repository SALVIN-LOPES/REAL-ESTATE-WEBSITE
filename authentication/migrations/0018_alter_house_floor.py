# Generated by Django 3.2.8 on 2022-01-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0017_auto_20220108_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='floor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

# Generated by Django 3.2.8 on 2021-12-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20211224_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
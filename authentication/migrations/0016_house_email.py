# Generated by Django 3.2.8 on 2022-01-02 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0015_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='email',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]

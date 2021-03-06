# Generated by Django 3.2.8 on 2021-11-05 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_customer_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('property_type', models.CharField(choices=[('1BHk', '1BHk'), ('2BHk', '2BHk'), ('3BHk', '3BHk'), ('4BHk', '4BHk')], max_length=200, null=True)),
                ('price', models.IntegerField(null=True)),
                ('view', models.CharField(choices=[('Side_View', 'Side_View'), ('Front_View', 'Front_View'), ('Back_View', 'Back_View')], max_length=200, null=True)),
                ('floor', models.IntegerField(null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('images', models.ImageField(upload_to='')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.customer')),
            ],
        ),
    ]

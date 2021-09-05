# Generated by Django 3.2.6 on 2021-08-28 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100)),
                ('business_contact', models.CharField(max_length=100)),
                ('business_email', models.EmailField(max_length=100)),
                ('business_website', models.URLField(max_length=100)),
                ('business_unit_number', models.CharField(max_length=100)),
                ('business_street_number', models.CharField(max_length=100)),
                ('business_street_name', models.CharField(max_length=100)),
                ('business_suburb', models.CharField(max_length=100)),
                ('business_postcode', models.CharField(max_length=100)),
                ('business_state', models.CharField(max_length=50)),
                ('business_country', models.CharField(max_length=50)),
                ('business_registered', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
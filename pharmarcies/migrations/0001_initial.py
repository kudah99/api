# Generated by Django 3.2.7 on 2022-02-17 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PharmaciesBranchDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('whatsapp_contact', models.CharField(max_length=15)),
                ('phonenumbers', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Pharmacies Branch Details',
            },
        ),
    ]
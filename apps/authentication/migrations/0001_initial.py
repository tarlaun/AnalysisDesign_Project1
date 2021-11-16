# Generated by Django 3.2.6 on 2021-11-15 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('document', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('location', models.CharField(blank=True, max_length=1000)),
                ('phone_number', models.CharField(max_length=11)),
            ],
        ),
    ]
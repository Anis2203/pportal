# Generated by Django 3.1.2 on 2020-12-10 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pinfo', models.CharField(max_length=20)),
                ('ptype', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('ammount', models.CharField(max_length=20)),
            ],
        ),
    ]

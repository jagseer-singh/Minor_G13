# Generated by Django 3.1 on 2020-11-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('body_part', models.CharField(max_length=200)),
                ('equipments', models.CharField(max_length=200)),
                ('difficulty', models.IntegerField()),
                ('procedure', models.TextField()),
            ],
        ),
    ]

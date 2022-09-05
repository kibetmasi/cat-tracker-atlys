# Generated by Django 4.1.1 on 2022-09-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatModel',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('timezone', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Cat Details',
            },
        ),
    ]
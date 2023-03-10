# Generated by Django 4.1.4 on 2022-12-23 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('address', models.TextField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('grade', models.IntegerField()),
                ('section', models.CharField(max_length=10)),
            ],
        ),
    ]

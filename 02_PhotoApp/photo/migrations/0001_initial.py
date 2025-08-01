# Generated by Django 5.2.4 on 2025-07-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]

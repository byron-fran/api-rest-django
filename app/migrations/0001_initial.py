# Generated by Django 4.2 on 2023-04-22 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_created=True)),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('tittle', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('technolody', models.TextField()),
            ],
        ),
    ]

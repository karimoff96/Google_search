# Generated by Django 3.2.7 on 2021-10-18 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_calc_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('user_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]

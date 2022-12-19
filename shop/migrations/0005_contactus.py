# Generated by Django 4.1.3 on 2022-12-18 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orderplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.EmailField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]

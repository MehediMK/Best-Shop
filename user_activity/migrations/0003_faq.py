# Generated by Django 4.1.3 on 2022-12-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_activity', '0002_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

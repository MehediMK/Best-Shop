# Generated by Django 4.1.3 on 2022-12-07 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
                ('category_image', models.ImageField(upload_to='category_image')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=250)),
                ('product_image', models.ImageField(upload_to='product_image')),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descrount_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_description', models.TextField(max_length=600)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.2 on 2023-04-26 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_image', models.FileField(default='', upload_to='products/images')),
                ('product_title', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
# Generated by Django 3.1.5 on 2021-02-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrendingProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trend_image', models.ImageField(blank=True, null=True, upload_to='TrendingProductImage')),
            ],
        ),
    ]

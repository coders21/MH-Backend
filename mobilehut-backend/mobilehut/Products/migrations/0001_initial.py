# Generated by Django 3.1.5 on 2021-01-20 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ModelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=300)),
                ('product_price', models.IntegerField(blank=True)),
                ('product_quantity', models.IntegerField(blank=True)),
                ('product_sku', models.CharField(blank=True, max_length=120)),
                ('product_description', models.CharField(blank=True, max_length=5000)),
                ('sale_price', models.IntegerField(blank=True)),
                ('saleprice_startdate', models.DateField(blank=True)),
                ('saleprice_enddate', models.DateField(blank=True)),
                ('product_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.brand')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.category')),
                ('product_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.modeltype')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('image_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour_name', models.CharField(blank=True, max_length=20)),
                ('colour_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product')),
            ],
        ),
    ]

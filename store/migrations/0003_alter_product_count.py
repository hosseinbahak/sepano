# Generated by Django 4.2 on 2023-04-13 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
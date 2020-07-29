# Generated by Django 3.0.8 on 2020-07-29 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_auto_20200729_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='image',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='terms',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
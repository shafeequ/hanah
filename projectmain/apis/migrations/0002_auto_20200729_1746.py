# Generated by Django 3.0.8 on 2020-07-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

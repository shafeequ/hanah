# Generated by Django 3.0.8 on 2020-07-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_auto_20200729_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='url',
            field=models.URLField(null=True),
        ),
    ]

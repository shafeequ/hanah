# Generated by Django 3.0.8 on 2020-07-29 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0011_auto_20200729_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='url',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20190706_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='article',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True, verbose_name='Longitude'),
        ),
    ]

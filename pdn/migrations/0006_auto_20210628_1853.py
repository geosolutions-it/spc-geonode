# Generated by Django 3.2.4 on 2021-06-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdn', '0005_auto_20210626_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='country_code',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='news',
            name='country_code',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.CharField(max_length=255),
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-30 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha',
            name='categoria',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]

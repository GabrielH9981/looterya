# Generated by Django 2.1.4 on 2020-10-25 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rifas', '0010_auto_20201024_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='rifa',
            name='ganhador',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rifa',
            name='tem_ganhador',
            field=models.BooleanField(default='False'),
            preserve_default=False,
        ),
    ]
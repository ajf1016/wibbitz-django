# Generated by Django 3.2.9 on 2021-12-06 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20211202_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketingfeature',
            name='image',
            field=models.FileField(upload_to='marketing/'),
        ),
    ]

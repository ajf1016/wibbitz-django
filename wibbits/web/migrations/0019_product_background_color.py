# Generated by Django 3.2.9 on 2021-12-29 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_auto_20211229_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='background_color',
            field=models.CharField(default='#ffc9b7', max_length=128),
            preserve_default=False,
        ),
    ]

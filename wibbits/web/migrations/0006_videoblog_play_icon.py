# Generated by Django 3.2.9 on 2021-12-02 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_blog_marketingfeature_product_testimonial_videoblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoblog',
            name='play_icon',
            field=models.FileField(default='abc', upload_to='blog/'),
            preserve_default=False,
        ),
    ]
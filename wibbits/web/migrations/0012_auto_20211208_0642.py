# Generated by Django 3.2.9 on 2021-12-08 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_blog_link_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('company', models.CharField(max_length=128)),
                ('company_size', models.CharField(choices=[('1', '1-10'), ('2', '11-50'), ('3', '51-200'), ('4', '201-500')], max_length=128)),
                ('industry', models.CharField(choices=[('1', 'Agriculture'), ('2', 'Banking & Finance'), ('3', 'Business Sevice & Software')], max_length=128)),
                ('job_role', models.CharField(choices=[('1', 'C-Suite'), ('2', 'VP')], max_length=128)),
                ('country', models.CharField(choices=[('us', 'United States'), ('albania', 'Albania')], max_length=128)),
                ('user_agreement', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelTable(
            name='blog',
            table='web_blog',
        ),
    ]
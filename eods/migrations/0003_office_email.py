# Generated by Django 3.1.7 on 2021-03-08 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eods', '0002_auto_20210228_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='email',
            field=models.EmailField(default='accounting@capstonedg.com', max_length=500),
        ),
    ]

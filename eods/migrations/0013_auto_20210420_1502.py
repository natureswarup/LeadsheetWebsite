# Generated by Django 3.1.7 on 2021-04-20 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eods', '0012_leadsheet_cash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadsheet',
            name='file_upload',
            field=models.FileField(upload_to='pdfs'),
        ),
        migrations.AlterField(
            model_name='office',
            name='email',
            field=models.EmailField(max_length=500),
        ),
    ]

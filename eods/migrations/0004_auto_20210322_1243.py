# Generated by Django 3.1.7 on 2021-03-22 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eods', '0003_office_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leadsheet',
            name='compassionate_finance',
        ),
        migrations.RemoveField(
            model_name='leadsheet',
            name='compassionate_finance_deposited',
        ),
    ]
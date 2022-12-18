# Generated by Django 4.1.4 on 2022-12-18 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
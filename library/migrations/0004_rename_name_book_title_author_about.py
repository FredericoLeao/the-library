# Generated by Django 4.1.4 on 2022-12-27 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_book_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]

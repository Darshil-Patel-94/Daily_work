# Generated by Django 5.2 on 2025-06-25 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlate', '0005_book_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
    ]

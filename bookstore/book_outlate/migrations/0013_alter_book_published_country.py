# Generated by Django 5.2.3 on 2025-06-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlate", "0012_country_alter_adress_options_book_published_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="published_country",
            field=models.ManyToManyField(
                related_name="books", to="book_outlate.country"
            ),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_company_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="address",
            field=models.TextField(
                blank=True, help_text="Full address of the company."
            ),
        ),
    ]

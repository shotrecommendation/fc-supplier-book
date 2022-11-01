# Generated by Django 4.1.2 on 2022-11-01 11:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="indicative_pricing",
        ),
        migrations.RemoveField(
            model_name="product",
            name="pricing_currency",
        ),
        migrations.AddField(
            model_name="company",
            name="description",
            field=models.TextField(
                default=None, help_text="Short description of the company."
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="company",
            name="last_modified",
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="address",
            field=models.CharField(
                help_text="Full address of the company.", max_length=256
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="date_of_foundation",
            field=models.DateField(help_text="Date of the company's foundation."),
        ),
        migrations.AlterField(
            model_name="company",
            name="name",
            field=models.CharField(help_text="Full company name.", max_length=100),
        ),
        migrations.AlterField(
            model_name="company",
            name="number_of_employees",
            field=models.PositiveIntegerField(
                blank=True, help_text="Approximate number of employees.", null=True
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="short_name",
            field=models.CharField(
                help_text="Shortened name of the company.", max_length=10
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="email",
            field=models.EmailField(max_length=64),
        ),
        migrations.AlterField(
            model_name="employee",
            name="job_title",
            field=models.CharField(help_text="Function in the company.", max_length=32),
        ),
        migrations.AlterField(
            model_name="product",
            name="company",
            field=models.ForeignKey(
                help_text="Company owning the product.",
                on_delete=django.db.models.deletion.PROTECT,
                to="catalog.company",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="model_name",
            field=models.CharField(
                help_text="Company's name for the product.", max_length=32
            ),
        ),
        migrations.AlterField(
            model_name="story",
            name="date",
            field=models.DateField(auto_now_add=True, help_text="Date of the entry."),
        ),
        migrations.AlterField(
            model_name="story",
            name="full_description",
            field=models.TextField(help_text="Full description of the event."),
        ),
        migrations.AlterField(
            model_name="story",
            name="title",
            field=models.CharField(
                help_text="Short summary of the entry.", max_length=128
            ),
        ),
        migrations.CreateModel(
            name="Roadmap",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "goal_title",
                    models.CharField(
                        help_text="Short summary of a general goal of a company.",
                        max_length=64,
                    ),
                ),
                ("additional_info", models.TextField()),
                (
                    "start_year",
                    models.PositiveIntegerField(
                        help_text="The year, that the work on this goal is planned to start."
                    ),
                ),
                (
                    "end_year",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="The year, that the work on this goal is planned to end.",
                        null=True,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.company",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pricing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(help_text="Date that the offer was made.")),
                (
                    "expiration_date",
                    models.DateField(help_text="Date that the offer will expire."),
                ),
                (
                    "indicative_pricing",
                    models.DecimalField(
                        decimal_places=2, help_text="indicative_pricing.", max_digits=16
                    ),
                ),
                (
                    "pricing_currency",
                    models.CharField(
                        choices=[("EUR", "EUR"), ("USD", "USD"), ("PLN", "PLN")],
                        help_text="Currency of the pricing.",
                        max_length=3,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FuelCell",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rated_power",
                    models.PositiveIntegerField(verbose_name="Rated power [kW]"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Battery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "total_energy",
                    models.PositiveIntegerField(verbose_name="Total energy [kWh]"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                    ),
                ),
            ],
        ),
    ]
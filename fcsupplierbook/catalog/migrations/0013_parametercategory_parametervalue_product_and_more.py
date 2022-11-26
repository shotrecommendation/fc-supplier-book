# Generated by Django 4.1.2 on 2022-11-26 20:35

import catalog.models.abstract
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0012_alter_roadmap_end_year_alter_roadmap_start_year"),
    ]

    operations = [
        migrations.CreateModel(
            name="ParameterCategory",
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
                    "name",
                    models.CharField(
                        help_text="Category of parameters.", max_length=32
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ParameterValue",
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
                ("value", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                    "model_name",
                    models.CharField(
                        help_text="Company's name for the product.", max_length=32
                    ),
                ),
                ("last_modified", models.DateField(auto_now=True)),
                (
                    "company",
                    models.ForeignKey(
                        help_text="Company owning the product.",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="catalog.company",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(models.Model, catalog.models.abstract.RecentMixin),
        ),
        migrations.CreateModel(
            name="ProductParameter",
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
                    "name",
                    models.CharField(
                        help_text="Name of the parameter, e.g. Length or Peak Power",
                        max_length=32,
                        unique=True,
                    ),
                ),
                (
                    "unit",
                    models.CharField(
                        default="-",
                        help_text="Unit of measurment if applies.",
                        max_length=10,
                    ),
                ),
                (
                    "is_key_parameter",
                    models.BooleanField(
                        default=False,
                        help_text="Decides if the parameter is important enough to include it in every summary view by default. If not, it will still be available in detailed views.",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="catalog.parametercategory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductType",
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
                    "full_name",
                    models.CharField(
                        help_text="Full name of a gneral category of products, eg. Battery or Engine, but not LTO Battery or Diesel Engine.",
                        max_length=20,
                        unique=True,
                    ),
                ),
                (
                    "short_name",
                    models.CharField(
                        help_text="A short name or abbreviation of the full name.",
                        max_length=3,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="batterypricing",
            name="product",
        ),
        migrations.RemoveField(
            model_name="fuelcell",
            name="company",
        ),
        migrations.RemoveField(
            model_name="fuelcellpricing",
            name="product",
        ),
        migrations.DeleteModel(
            name="Battery",
        ),
        migrations.DeleteModel(
            name="BatteryPricing",
        ),
        migrations.DeleteModel(
            name="FuelCell",
        ),
        migrations.DeleteModel(
            name="FuelCellPricing",
        ),
        migrations.AddField(
            model_name="productparameter",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="catalog.producttype"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="catalog.producttype"
            ),
        ),
        migrations.AddField(
            model_name="parametervalue",
            name="parameter_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.productparameter",
            ),
        ),
        migrations.AddField(
            model_name="parametervalue",
            name="product",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="catalog.product"
            ),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-03 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="batterypricing",
            old_name="date",
            new_name="received_date",
        ),
        migrations.RenameField(
            model_name="fuelcellpricing",
            old_name="date",
            new_name="received_date",
        ),
        migrations.RemoveField(
            model_name="company",
            name="last_modified",
        ),
        migrations.AddField(
            model_name="battery",
            name="last_modified",
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name="batterypricing",
            name="volume",
            field=models.PositiveIntegerField(
                default=0, help_text="Volume on which the offer is based."
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="fuelcell",
            name="last_modified",
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name="fuelcellpricing",
            name="volume",
            field=models.PositiveIntegerField(
                default=0, help_text="Volume on which the offer is based."
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="batterypricing",
            name="indicative_pricing",
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
        migrations.AlterField(
            model_name="fuelcellpricing",
            name="indicative_pricing",
            field=models.DecimalField(decimal_places=2, max_digits=16),
        ),
    ]
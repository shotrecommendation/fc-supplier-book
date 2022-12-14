# Generated by Django 4.1.2 on 2022-11-26 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0011_alter_employee_first_name_alter_employee_last_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roadmap",
            name="end_year",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="The year, that the work on this goal is planned to be achieved by.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="roadmap",
            name="start_year",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="The year, that the work on this goal is planned to start.",
                null=True,
            ),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0009_alter_employee_first_name_alter_employee_last_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="function",
            field=models.CharField(
                choices=[
                    ("SERV", "serviceman"),
                    ("ENGI", "engineer"),
                    ("SALE", "salesman"),
                    ("MANA", "management"),
                    ("RCPT", "reception"),
                    ("SECU", "security"),
                    ("UNKN", "unknown"),
                ],
                default="UNKN",
                help_text="Function in the company.",
                max_length=4,
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="phone_number",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]

# Generated by Django 2.2.12 on 2022-04-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maasserver", "0273_ipaddress_defaults"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="endpoint",
            field=models.IntegerField(
                choices=[(0, "API"), (1, "WebUI"), (2, "CLI")],
                default=0,
                editable=False,
            ),
        ),
    ]

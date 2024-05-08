# Generated by Django 4.2.11 on 2024-05-08 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("commissions", "0003_commission_job_jobapplication_delete_comments_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="commission",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="job",
                to="commissions.commission",
            ),
        ),
    ]

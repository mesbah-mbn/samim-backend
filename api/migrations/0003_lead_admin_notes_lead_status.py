# Generated manually for admin lead workflow fields.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_lead_email_alter_lead_message"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="admin_notes",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="lead",
            name="status",
            field=models.CharField(
                choices=[
                    ("new", "New"),
                    ("contacted", "Contacted"),
                    ("offer_sent", "Offer sent"),
                    ("won", "Won"),
                    ("lost", "Lost"),
                ],
                default="new",
                max_length=20,
            ),
        ),
    ]

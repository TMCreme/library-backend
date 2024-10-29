# Generated by Django 4.2 on 2024-09-25 11:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=200)),
                ("isbn", models.CharField(max_length=30)),
                ("date_published", models.DateField()),
                ("publisher", models.CharField(max_length=100)),
            ],
        ),
    ]

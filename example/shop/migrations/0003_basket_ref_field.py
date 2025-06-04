from uuid import uuid4
from django.db import migrations, models
from django.utils.translation import gettext_lazy as _

class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_rename_owner_field"),
    ]

    operations = [
        migrations.AddField(
            model_name="basket",
            name="ref",
            field=models.CharField(max_length=128, unique=True, default=uuid4, verbose_name=_("Reference")),
        ),
    ]

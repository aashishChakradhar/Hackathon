
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_rename_id_skillset_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skillset',
            old_name='user',
            new_name='id',
        ),
    ]

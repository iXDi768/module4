

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_advertisement_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisements',
        ),
    ]

from django.db import migrations
from django.core.management import call_command

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.RunPython(call_command('collectstatic', '--noinput'))
    ]

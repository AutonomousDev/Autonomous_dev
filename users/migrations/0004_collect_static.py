from django.db import migrations
from django.core.management import call_command

def run_collect_static(args, options):
    call_command('collectstatic', '--noinput')


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.RunPython(run_collect_static)
    ]

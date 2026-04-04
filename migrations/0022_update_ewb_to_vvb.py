from django.db import migrations
import swapper


def update_ewb_to_vvb(apps, schema_editor):
    """
    Update the residence code for EWS Bhawan (ewb) to Vivekananda Bhawan (vvb).
    """
    Residence = swapper.load_model('kernel', 'Residence')
    Residence.objects.filter(code='ewb').update(code='vvb')


class Migration(migrations.Migration):

    dependencies = [
        ('shell', '0021_alter_centre_code_alter_degree_code_and_more'),
    ]

    operations = [
        migrations.RunPython(update_ewb_to_vvb, reverse_code=migrations.RunPython.noop),
    ]

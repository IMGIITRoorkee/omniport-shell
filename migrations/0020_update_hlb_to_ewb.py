from django.db import migrations
import swapper


def update_hlb_to_ewb(apps, schema_editor):
    Residence = swapper.load_model('kernel','Residence')
    Residence.objects.filter(code='hlb').update(code='ewb')


class Migration(migrations.Migration):

    dependencies = [
        ('shell', '0019_alter_residence_code'),
    ]

    operations = [
        migrations.RunPython(update_hlb_to_ewb, reverse_code=migrations.RunPython.noop),
    ]
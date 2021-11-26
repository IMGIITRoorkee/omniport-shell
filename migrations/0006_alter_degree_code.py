# Generated by Django 3.2.8 on 2021-11-26 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shell', '0005_auto_20200110_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree',
            name='code',
            field=models.CharField(choices=[('btech', 'B.Tech. - Bachelor of Technology'), ('idd', 'Int. M.Tech. - Integrated Dual Degree'), ('bsc', 'B.Sc. - Bachelor of Science'), ('barch', 'B.Arch. - Bachelor of Architecture'), ('imsc', 'Int. M.Sc. - Integrated Master of Science'), ('imt', 'Int. M.Tech - Integrated Master of Technology'), ('bsms', 'BS-MS - Bachelor of Science - Master of Science'), ('mtech', 'M.Tech. - Master of Technology'), ('msc', 'M.Sc. - Master of Science'), ('march', 'M.Arch. - Master of Architecture'), ('murp', 'M.U.R.P - Master of Urban and Regional Planning'), ('pgdip', 'P.G. Dip. - Post-graduate Diploma'), ('mba', 'M.B.A. - Master of Business Administration'), ('mca', 'M.C.A. - Master of Computer Applications'), ('phd', 'Ph.D. - Doctor of Philosophy'), ('pdoc', 'Post Doc. - Post-doctorate')], max_length=7, unique=True),
        ),
    ]

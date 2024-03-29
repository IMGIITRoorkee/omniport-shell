# Generated by Django 4.1.5 on 2023-01-19 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shell', '0009_alter_residence_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='code',
            field=models.CharField(choices=[('ased', 'Applied Science and Engineering Department'), ('amsc', 'Applied Mathematics and Scientific Computing'), ('arcd', 'Architecture and Planning Department'), ('btd', 'Biotechnology Department'), ('ched', 'Chemical Engineering Department'), ('cyd', 'Chemistry Department'), ('ced', 'Civil Engineering Department'), ('csed', 'Computer Science and Engineering Department'), ('dd', 'Department of Design'), ('esd', 'Earth Sciences Department'), ('eqd', 'Earthquake Department'), ('eed', 'Electrical Engineering Department'), ('eced', 'Electronics and Communication Engineering Department'), ('hsd', 'Humanities and Social Sciences Department'), ('hyd', 'Hydrology Department'), ('hred', 'Hydro and Renewable Energy Department'), ('msd', 'Management Studies Department'), ('mad', 'Mathematics Department'), ('mied', 'Mechanical and Industrial Engineering Department'), ('mmed', 'Metallurgical and Materials Engineering Department'), ('ptd', 'Paper Technology Department'), ('phd', 'Physics Department'), ('pped', 'Polymer and Process Engineering Department'), ('wrdmd', 'Water Resources Development and Management Department'), ('qip', 'Quality Improvement Programme')], max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='residence',
            name='code',
            field=models.CharField(choices=[('azb', 'Azad bhawan'), ('ctb', 'Cautley bhawan'), ('gnb', 'Ganga bhawan'), ('gvb', 'Govind bhawan'), ('jlb', 'Jawahar bhawan'), ('mvb', 'Malviya bhawan'), ('rkb', 'Radhakrishnan bhawan'), ('rjb', 'Rajendra bhawan'), ('rgb', 'Rajiv bhawan'), ('rvb', 'Ravindra bhawan'), ('hlb', 'Himalaya bhawan (boys)'), ('snb', 'Sarojini bhawan'), ('kgb', 'Kasturba bhawan'), ('igb', ' Indira bhawan'), ('vbg', 'Vigyan bhawan (girls)'), ('hia', 'Himgiri apartment'), ('hlg', 'Himalaya bhawan (girls)'), ('gph', 'G.P. hostel'), ('mrc', 'M.R. Chopra hostel'), ('azw', 'Azad wing'), ('dsb', 'D.S. Barrack hostel'), ('ank', 'A.N. Khosla house'), ('khs', 'Khosla international house (stay)'), ('mhs', 'Married hostel Saharanpur campus'), ('ncn', 'N.C. Nigam house'), ('fah', 'Faculty home'), ('khg', 'Khosla international house (guest)'), ('vig', 'Vigyan kunj'), ('vik', 'Vikas nagar'), ('nit', 'Niti nagar'), ('jkh', 'Jai Krishna house'), ('shi', 'Shivalik apartments'), ('hva', 'Hill view apartments'), ('oth', "Old teachers' hostel"), ('far', 'Faculty residences'), ('doc', 'Doctoral residences'), ('nor', 'Non-resident')], max_length=3, unique=True),
        ),
    ]

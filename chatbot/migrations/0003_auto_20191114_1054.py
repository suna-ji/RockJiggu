# Generated by Django 2.2.6 on 2019-11-14 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_auto_20191114_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='returninfo',
            name='is_agency',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='returninfo',
            name='is_clearance',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='returninfo',
            name='is_received',
            field=models.BooleanField(null=True),
        ),
    ]

# Generated by Django 2.0.9 on 2019-02-14 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.ForeignKey(blank=True, limit_choices_to={'parent': False}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='website.Service'),
        ),
    ]

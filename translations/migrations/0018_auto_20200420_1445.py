# Generated by Django 3.0.5 on 2020-04-20 06:45

import adminsortable.fields
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0017_auto_20200420_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phrase',
            name='category',
            field=adminsortable.fields.SortableForeignKey(on_delete=django.db.models.deletion.CASCADE, to='translations.Category'),
        ),
    ]

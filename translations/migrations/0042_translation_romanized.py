# Generated by Django 3.0.5 on 2020-04-29 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0041_downloadable_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='romanized',
            field=models.TextField(blank=True),
        ),
    ]
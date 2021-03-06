# Generated by Django 3.0.5 on 2020-04-21 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0026_auto_20200421_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phrase',
            name='categories',
            field=models.ManyToManyField(related_name='phrase', related_query_name='phrases', through='translations.PhraseCategory', to='translations.Category'),
        ),
    ]

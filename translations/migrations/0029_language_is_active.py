# Generated by Django 3.0.5 on 2020-04-21 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0028_auto_20200422_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-25 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0037_translationfeedback_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent_category',
        ),
    ]

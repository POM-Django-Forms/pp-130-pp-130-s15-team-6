# Generated by Django 4.1 on 2025-06-20 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='issue_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

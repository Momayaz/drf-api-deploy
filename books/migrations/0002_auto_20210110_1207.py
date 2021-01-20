# Generated by Django 3.1.5 on 2021-01-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='book',
            name='writer',
            field=models.CharField(default=' ', max_length=64),
            preserve_default=False,
        ),
    ]
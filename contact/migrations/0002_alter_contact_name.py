# Generated by Django 3.2.7 on 2021-09-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.TextField(),
        ),
    ]

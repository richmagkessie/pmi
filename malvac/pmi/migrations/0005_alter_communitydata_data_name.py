# Generated by Django 4.0 on 2023-10-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmi', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitydata',
            name='data_name',
            field=models.FileField(upload_to='data_files/'),
        ),
    ]

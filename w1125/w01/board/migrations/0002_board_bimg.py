# Generated by Django 5.1.3 on 2024-11-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='bimg',
            field=models.ImageField(null=True, upload_to='board'),
        ),
    ]

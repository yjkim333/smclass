# Generated by Django 5.1.3 on 2024-12-05 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='like_members',
            field=models.ManyToManyField(default='', related_name='like_member', to='member.member'),
        ),
    ]

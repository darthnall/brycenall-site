# Generated by Django 5.0.4 on 2024-05-14 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_delete_newslettersignupform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='desc',
            field=models.TextField(default='', max_length=2048),
        ),
    ]

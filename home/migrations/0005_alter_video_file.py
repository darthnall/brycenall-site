# Generated by Django 5.0.4 on 2024-05-12 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_video_remove_newslettersignupform_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(storage='video', upload_to=''),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-13 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_video_duration_video_date_uploaded'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='file',
            new_name='source',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='video',
            name='date_uploaded',
        ),
        migrations.AddField(
            model_name='video',
            name='desc',
            field=models.TextField(default='', max_length=2048),
            preserve_default=False,
        ),
    ]

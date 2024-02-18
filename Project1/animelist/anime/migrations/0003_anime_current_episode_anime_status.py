# Generated by Django 5.0.2 on 2024-02-17 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_animes'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='current_episode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='status',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]

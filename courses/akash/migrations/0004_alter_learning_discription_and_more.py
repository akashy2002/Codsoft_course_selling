# Generated by Django 4.1.7 on 2023-06-04 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akash', '0003_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning',
            name='discription',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='prerequisite',
            name='discription',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='discription',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=100),
        ),
    ]
# Generated by Django 3.2.10 on 2021-12-28 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobstory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskhistory',
            name='copies',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='taskhistory',
            name='job_number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='taskhistory',
            name='job_result_detail',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='taskhistory',
            name='pages',
            field=models.PositiveSmallIntegerField(),
        ),
    ]

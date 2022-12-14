# Generated by Django 4.0.5 on 2022-09-12 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_dungeon_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='dungeon_name',
            field=models.CharField(max_length=30, verbose_name='Dungeon name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Email Address'),
        ),
    ]

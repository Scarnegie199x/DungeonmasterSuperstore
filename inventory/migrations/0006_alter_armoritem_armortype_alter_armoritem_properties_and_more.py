# Generated by Django 4.0.5 on 2022-09-13 15:22

from django.db import migrations, models
import profanity.validators


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_armoritem_description_alter_armoritem_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armoritem',
            name='armortype',
            field=models.CharField(max_length=15, validators=[profanity.validators.validate_is_profane], verbose_name='Armor type'),
        ),
        migrations.AlterField(
            model_name='armoritem',
            name='properties',
            field=models.CharField(max_length=200, validators=[profanity.validators.validate_is_profane]),
        ),
        migrations.AlterField(
            model_name='potionitem',
            name='properties',
            field=models.CharField(default=False, max_length=200, validators=[profanity.validators.validate_is_profane]),
        ),
        migrations.AlterField(
            model_name='spellitem',
            name='casting_time',
            field=models.CharField(max_length=50, validators=[profanity.validators.validate_is_profane], verbose_name='Casting time'),
        ),
        migrations.AlterField(
            model_name='spellitem',
            name='components',
            field=models.CharField(max_length=50, validators=[profanity.validators.validate_is_profane]),
        ),
        migrations.AlterField(
            model_name='spellitem',
            name='duration',
            field=models.CharField(max_length=50, validators=[profanity.validators.validate_is_profane]),
        ),
        migrations.AlterField(
            model_name='spellitem',
            name='higher_levels',
            field=models.CharField(max_length=200, validators=[profanity.validators.validate_is_profane], verbose_name='Higher level cast'),
        ),
        migrations.AlterField(
            model_name='spellitem',
            name='range',
            field=models.CharField(max_length=50, validators=[profanity.validators.validate_is_profane]),
        ),
        migrations.AlterField(
            model_name='spellitem',
            name='school',
            field=models.CharField(max_length=50, validators=[profanity.validators.validate_is_profane]),
        ),
        migrations.AlterField(
            model_name='spellitem',
            name='spell_level',
            field=models.CharField(max_length=10, validators=[profanity.validators.validate_is_profane], verbose_name='Spell level'),
        ),
        migrations.AlterField(
            model_name='spellitem',
            name='spell_lists',
            field=models.CharField(max_length=100, validators=[profanity.validators.validate_is_profane], verbose_name='Spell list'),
        ),
        migrations.AlterField(
            model_name='spellitem',
            name='target',
            field=models.CharField(max_length=50, validators=[profanity.validators.validate_is_profane]),
        ),
        migrations.AlterField(
            model_name='wonderousitem',
            name='properties',
            field=models.CharField(default=False, max_length=200, validators=[profanity.validators.validate_is_profane]),
        ),
    ]

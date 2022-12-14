# Generated by Django 4.0.5 on 2022-09-12 19:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armoritem',
            name='armortype',
            field=models.CharField(max_length=15, verbose_name='Armor type'),
        ),
        migrations.AlterField(
            model_name='armoritem',
            name='bonus',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='armoritem',
            name='category',
            field=models.CharField(choices=[('heavy', 'Heavy'), ('medium', 'Medium'), ('light', 'Light')], max_length=15),
        ),
        migrations.AlterField(
            model_name='spellitem',
            name='spell_level',
            field=models.CharField(max_length=10, verbose_name='Spell level'),
        ),
        migrations.AlterField(
            model_name='spellitem',
            name='target',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='weaponitem',
            name='attack',
            field=models.CharField(choices=[('melee', 'Melee'), ('ranged', 'Ranged')], max_length=10),
        ),
        migrations.AlterField(
            model_name='weaponitem',
            name='bonus',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='weaponitem',
            name='category',
            field=models.CharField(choices=[('simple', 'Simple'), ('martial', 'Martial')], max_length=10),
        ),
        migrations.AlterField(
            model_name='weaponitem',
            name='damage',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='weaponitem',
            name='damagetype',
            field=models.CharField(choices=[('slashing', 'Slashing'), ('bludgeoning', 'Bludgeoning'), ('piercing', 'Piercing')], max_length=20, verbose_name='Damage type'),
        ),
        migrations.AlterField(
            model_name='weaponitem',
            name='weapontype',
            field=models.CharField(max_length=20, verbose_name='Weapon type'),
        ),
    ]

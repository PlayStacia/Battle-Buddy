# Generated by Django 3.2.3 on 2021-07-07 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('battlebuddyapp', '0002_participant_initiative'),
    ]

    operations = [
        migrations.CreateModel(
            name='Affliction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Boon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Statblock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('initiative_bonus', models.IntegerField()),
                ('armor_class', models.IntegerField()),
                ('hit_points', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('dexterity', models.IntegerField()),
                ('constitution', models.IntegerField()),
                ('intelligence', models.IntegerField()),
                ('wisdom', models.IntegerField()),
                ('charisma', models.IntegerField()),
                ('xp', models.IntegerField()),
                ('special_abilities', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('details', models.TextField(blank=True)),
                ('attack_methods', models.ManyToManyField(blank=True, related_name='attack_methods', to='battlebuddyapp.AttackMethod')),
                ('condition_immunities', models.ManyToManyField(blank=True, related_name='immune_species', to='battlebuddyapp.ConditionType')),
                ('damage_immunities', models.ManyToManyField(blank=True, related_name='immune_species', to='battlebuddyapp.DamageType')),
                ('damage_resistances', models.ManyToManyField(blank=True, related_name='resistant_species', to='battlebuddyapp.DamageType')),
                ('damage_vulnerabilities', models.ManyToManyField(blank=True, related_name='vulnerable_species', to='battlebuddyapp.DamageType')),
            ],
        ),
        migrations.RemoveField(
            model_name='participant',
            name='species',
        ),
        migrations.AddField(
            model_name='participant',
            name='armour',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='health',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Species',
        ),
        migrations.AddField(
            model_name='participant',
            name='afflictions',
            field=models.ManyToManyField(blank=True, related_name='afflictied', to='battlebuddyapp.Affliction'),
        ),
        migrations.AddField(
            model_name='participant',
            name='boons',
            field=models.ManyToManyField(blank=True, related_name='booned', to='battlebuddyapp.Boon'),
        ),
        migrations.AddField(
            model_name='participant',
            name='statblock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='battlebuddyapp.statblock'),
        ),
    ]

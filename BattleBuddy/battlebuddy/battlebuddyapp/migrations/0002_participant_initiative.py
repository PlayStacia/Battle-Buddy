# Generated by Django 3.2.3 on 2021-07-06 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battlebuddyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='initiative',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
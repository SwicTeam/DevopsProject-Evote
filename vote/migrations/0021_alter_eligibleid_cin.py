# Generated by Django 3.2.9 on 2021-12-14 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0020_alter_eligibleid_cin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eligibleid',
            name='cin',
            field=models.BigIntegerField(null=True),
        ),
    ]

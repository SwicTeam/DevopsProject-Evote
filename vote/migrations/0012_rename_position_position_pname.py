# Generated by Django 3.2.9 on 2021-12-09 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0011_alter_votingprocess_voting_process'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='position',
            new_name='pname',
        ),
    ]

# Generated by Django 3.2 on 2021-05-11 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210505_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpu',
            old_name='CPU_cores',
            new_name='cpu_cores',
        ),
        migrations.RenameField(
            model_name='cpu',
            old_name='CPU_series',
            new_name='cpu_series',
        ),
        migrations.RenameField(
            model_name='cpu',
            old_name='CPU_socket',
            new_name='cpu_socket',
        ),
        migrations.RenameField(
            model_name='cpu',
            old_name='CPU_speed',
            new_name='cpu_speed',
        ),
        migrations.RenameField(
            model_name='cpu',
            old_name='CPU_turbo_speed',
            new_name='cpu_turbo_speed',
        ),
        migrations.RenameField(
            model_name='cpu',
            old_name='L3_Cache',
            new_name='l3_Cache',
        ),
    ]

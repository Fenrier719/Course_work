# Generated by Django 3.2 on 2021-05-11 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20210511_1122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motherboard',
            old_name='amount_of_DisplayPort',
            new_name='amount_of_displayport',
        ),
        migrations.RenameField(
            model_name='motherboard',
            old_name='amount_of_HDMI',
            new_name='amount_of_hdmi',
        ),
        migrations.RenameField(
            model_name='motherboard',
            old_name='amount_of_slots_for_RAM',
            new_name='amount_of_slots_for_ram',
        ),
        migrations.RenameField(
            model_name='motherboard',
            old_name='amount_of_USB',
            new_name='amount_of_usb',
        ),
        migrations.RenameField(
            model_name='motherboard',
            old_name='amount_of_VGA',
            new_name='amount_of_vga',
        ),
        migrations.RenameField(
            model_name='motherboard',
            old_name='max_speed_of_RAM',
            new_name='max_speed_of_ram',
        ),
    ]

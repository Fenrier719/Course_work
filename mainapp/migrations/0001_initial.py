# Generated by Django 3.2 on 2021-04-26 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('D', 'Dialog'), ('C', 'Chat')], default='D', max_length=1, verbose_name='Тип')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Участник')),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.TextField(max_length=50)),
                ('manufacturer', models.TextField(max_length=50)),
                ('ram_technology', models.TextField(max_length=50)),
                ('ram_speed', models.PositiveIntegerField()),
                ('capacity', models.PositiveIntegerField()),
                ('number_of_modules', models.PositiveIntegerField()),
                ('release_year', models.PositiveIntegerField()),
                ('computer_id', models.ManyToManyField(to='mainapp.Computer')),
            ],
        ),
        migrations.CreateModel(
            name='PowerBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.TextField(max_length=50)),
                ('model', models.TextField(max_length=50)),
                ('power', models.PositiveIntegerField()),
                ('form_factor', models.TextField(max_length=50)),
                ('kpd', models.PositiveIntegerField()),
                ('motherboard_power', models.TextField(max_length=50)),
                ('release_year', models.PositiveIntegerField()),
                ('computer_id', models.ManyToManyField(to='mainapp.Computer')),
            ],
        ),
        migrations.CreateModel(
            name='MotherBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.TextField(max_length=50)),
                ('model', models.TextField(max_length=50)),
                ('ram_type', models.TextField(max_length=50)),
                ('form_factor', models.TextField(max_length=50)),
                ('amount_of_slots_for_RAM', models.PositiveIntegerField()),
                ('date_of_release', models.TextField(max_length=50)),
                ('socket', models.TextField(max_length=50)),
                ('amount_of_USB', models.PositiveIntegerField()),
                ('amount_of_HDMI', models.PositiveIntegerField()),
                ('amount_of_DisplayPort', models.PositiveIntegerField()),
                ('amount_of_VGA', models.PositiveIntegerField()),
                ('max_speed_of_RAM', models.PositiveIntegerField()),
                ('release_year', models.PositiveIntegerField()),
                ('computer_id', models.ManyToManyField(to='mainapp.Computer')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата сообщения')),
                ('is_read', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.chat', verbose_name='Чат')),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='HDD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.TextField(max_length=50)),
                ('manufacturer', models.TextField(max_length=50)),
                ('cache', models.PositiveIntegerField()),
                ('spindle_speed', models.PositiveIntegerField()),
                ('interface_type', models.TextField(max_length=50)),
                ('capacity', models.PositiveIntegerField()),
                ('form_factor', models.TextField(max_length=50)),
                ('release_year', models.PositiveIntegerField()),
                ('computer_id', models.ManyToManyField(to='mainapp.Computer')),
            ],
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.TextField(max_length=50)),
                ('chipset', models.TextField(max_length=50)),
                ('VRAM', models.PositiveIntegerField()),
                ('release_year', models.PositiveIntegerField()),
                ('vram_type', models.TextField(max_length=50)),
                ('effective_speed', models.PositiveIntegerField()),
                ('recommended_power', models.PositiveIntegerField()),
                ('computer_id', models.ManyToManyField(to='mainapp.Computer')),
            ],
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.TextField(max_length=50)),
                ('CPU_series', models.TextField(max_length=50)),
                ('threads', models.PositiveIntegerField()),
                ('CPU_speed', models.PositiveIntegerField()),
                ('CPU_cores', models.PositiveIntegerField()),
                ('CPU_socket', models.TextField(max_length=50)),
                ('CPU_turbo_speed', models.PositiveIntegerField()),
                ('L3_Cache', models.PositiveIntegerField()),
                ('unlocked_multiplier', models.BooleanField()),
                ('release_year', models.PositiveIntegerField()),
                ('computer_id', models.ManyToManyField(to='mainapp.Computer')),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.TextField(max_length=50)),
                ('model', models.TextField(max_length=50)),
                ('color', models.TextField(max_length=50)),
                ('form_factor', models.TextField(max_length=50)),
                ('material', models.TextField(max_length=50)),
                ('height', models.PositiveIntegerField()),
                ('width', models.PositiveIntegerField()),
                ('depth', models.PositiveIntegerField()),
                ('max_size_of_motherboard', models.TextField()),
                ('release_year', models.PositiveIntegerField()),
                ('computer_id', models.ManyToManyField(to='mainapp.Computer')),
            ],
        ),
    ]
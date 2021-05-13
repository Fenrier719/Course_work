# Generated by Django 3.2 on 2021-05-11 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedComputer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Изображение')),
                ('name', models.TextField(default='', max_length=50, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'DeletedComputer',
            },
        ),
        migrations.CreateModel(
            name='DeletedRAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.TextField(max_length=50, verbose_name='Модель')),
                ('manufacturer', models.TextField(max_length=50, verbose_name='Изготовитель')),
                ('ram_technology', models.TextField(max_length=50, verbose_name='Технология')),
                ('ram_speed', models.PositiveIntegerField(verbose_name='Частота памяти, МГц')),
                ('capacity', models.PositiveIntegerField(verbose_name='Емкость, Гб')),
                ('number_of_modules', models.PositiveIntegerField(verbose_name='Количество модулей')),
                ('release_year', models.PositiveIntegerField(verbose_name='Год релиза')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Изображение')),
                ('computer_id', models.ManyToManyField(blank=True, related_name='related_RAM', to='triggers.DeletedComputer')),
            ],
            options={
                'verbose_name': 'DeletedRAM',
            },
        ),
        migrations.CreateModel(
            name='DeletedPowerBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.TextField(max_length=50, verbose_name='Изготовитель')),
                ('model', models.TextField(max_length=50, verbose_name='Модель')),
                ('power', models.PositiveIntegerField(verbose_name='Мощность, Вт')),
                ('form_factor', models.TextField(max_length=50, verbose_name='Форм-фактор')),
                ('kpd', models.PositiveIntegerField(verbose_name='КПД, %')),
                ('motherboard_power', models.TextField(max_length=50, verbose_name='Питание платы')),
                ('release_year', models.PositiveIntegerField(verbose_name='Год релиза')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Изображение')),
                ('computer_id', models.ManyToManyField(blank=True, related_name='related_PowerBlock', to='triggers.DeletedComputer')),
            ],
            options={
                'verbose_name': 'DeletedPowerBlock',
            },
        ),
        migrations.CreateModel(
            name='DeletedMotherBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.TextField(max_length=50, verbose_name='Изготовитель')),
                ('model', models.TextField(max_length=50, verbose_name='Модель')),
                ('ram_type', models.TextField(max_length=50, verbose_name='Тип памяти')),
                ('form_factor', models.TextField(max_length=50, verbose_name='Форм-фактор')),
                ('amount_of_slots_for_ram', models.PositiveIntegerField(verbose_name='Количество слотов памяти')),
                ('socket', models.TextField(max_length=50, verbose_name='Сокет')),
                ('amount_of_usb', models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество портов USB')),
                ('amount_of_hdmi', models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество портов HDMI')),
                ('amount_of_displayport', models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество портов DisplayPort')),
                ('amount_of_vga', models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество портов VGA')),
                ('max_speed_of_ram', models.PositiveIntegerField(verbose_name='Максимальная частота памяти, МГц')),
                ('release_year', models.PositiveIntegerField(verbose_name='Год релиза')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Изображение')),
                ('computer_id', models.ManyToManyField(blank=True, related_name='related_MotherBoard', to='triggers.DeletedComputer')),
            ],
            options={
                'verbose_name': 'DeletedMotherBoard',
            },
        ),
        migrations.CreateModel(
            name='DeletedHDD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.TextField(max_length=50, verbose_name='Модель')),
                ('manufacturer', models.TextField(max_length=50, verbose_name='Изготовитель')),
                ('cache', models.PositiveIntegerField(verbose_name='Кэш, Мб')),
                ('spindle_speed', models.PositiveIntegerField(verbose_name='Скорость винта, обр/мин')),
                ('interface_type', models.TextField(max_length=50, verbose_name='Тип интерфейса')),
                ('capacity', models.PositiveIntegerField(verbose_name='Емкость, Тб')),
                ('form_factor', models.TextField(max_length=50, verbose_name='Форм-фактор')),
                ('release_year', models.PositiveIntegerField(verbose_name='Год релиза')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Изображение')),
                ('computer_id', models.ManyToManyField(blank=True, related_name='related_HDD', to='triggers.DeletedComputer')),
            ],
            options={
                'verbose_name': 'DeletedHDD',
            },
        ),
        migrations.CreateModel(
            name='DeletedGPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.TextField(max_length=50, verbose_name='Изготовитель')),
                ('chipset', models.TextField(max_length=50, verbose_name='Чипсет')),
                ('VRAM', models.PositiveIntegerField(verbose_name='Видеопамять, Гб')),
                ('release_year', models.PositiveIntegerField(verbose_name='Год релиза')),
                ('vram_type', models.TextField(max_length=50, verbose_name='Тип видеопамяти')),
                ('effective_speed', models.PositiveIntegerField(verbose_name='Эффетивная частота МГц, ')),
                ('recommended_power', models.PositiveIntegerField(verbose_name='Рекомендуемая можность БП, Вт')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Изображение')),
                ('computer_id', models.ManyToManyField(blank=True, related_name='related_GPU', to='triggers.DeletedComputer')),
            ],
            options={
                'verbose_name': 'DeletedGPU',
            },
        ),
        migrations.CreateModel(
            name='DeletedCPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.TextField(max_length=50, verbose_name='Изготовитель')),
                ('cpu_series', models.TextField(max_length=50, verbose_name='Серия')),
                ('threads', models.PositiveIntegerField(verbose_name='Количество потоков')),
                ('cpu_speed', models.PositiveIntegerField(verbose_name='Частота, МГц')),
                ('cpu_cores', models.PositiveIntegerField(verbose_name='Количество ядер')),
                ('cpu_socket', models.TextField(max_length=50, verbose_name='Сокет')),
                ('cpu_turbo_speed', models.PositiveIntegerField(verbose_name='Максимальная тактовая частота, МГц')),
                ('l3_Cache', models.PositiveIntegerField(verbose_name='Кэш, Мб')),
                ('unlocked_multiplier', models.BooleanField(verbose_name='Возможность для разгона')),
                ('release_year', models.PositiveIntegerField(verbose_name='Год релиза')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Изображение')),
                ('computer_id', models.ManyToManyField(blank=True, related_name='related_CPU', to='triggers.DeletedComputer')),
            ],
            options={
                'verbose_name': 'DeletedCPU',
            },
        ),
        migrations.CreateModel(
            name='DeletedCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.TextField(max_length=50, verbose_name='Изготовитель')),
                ('model', models.TextField(max_length=50, verbose_name='Модель')),
                ('color', models.TextField(max_length=50, verbose_name='Цвет')),
                ('form_factor', models.TextField(max_length=50, verbose_name='Форм-фактор')),
                ('material', models.TextField(max_length=50, verbose_name='Материал')),
                ('height', models.PositiveIntegerField(verbose_name='Высота, мм')),
                ('width', models.PositiveIntegerField(verbose_name='Ширина, мм')),
                ('depth', models.PositiveIntegerField(verbose_name='Глубина, мм')),
                ('max_size_of_motherboard', models.TextField(verbose_name='Максимальный размер материнской платы')),
                ('release_year', models.PositiveIntegerField(verbose_name='Год релиза')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Изображение')),
                ('computer_id', models.ManyToManyField(blank=True, related_name='related_Case', to='triggers.DeletedComputer')),
            ],
            options={
                'verbose_name': 'DeletedCase',
            },
        ),
    ]

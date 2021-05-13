from django.db import models


class DeletedComputer(models.Model):
    image = models.ImageField(null=True, verbose_name='Изображение')
    name = models.TextField(max_length=50, verbose_name='Наименование', default='')

    class Meta:
        verbose_name = 'DeletedComputer'


class DeletedGPU(models.Model):
    manufacturer = models.TextField(max_length=50, verbose_name='Изготовитель')
    chipset = models.TextField(max_length=50, verbose_name='Чипсет')
    VRAM = models.PositiveIntegerField(verbose_name='Видеопамять, Гб')
    release_year = models.PositiveIntegerField(verbose_name='Год релиза')
    vram_type = models.TextField(max_length=50, verbose_name='Тип видеопамяти')
    effective_speed = models.PositiveIntegerField(verbose_name='Эффетивная частота МГц, ')
    recommended_power = models.PositiveIntegerField(verbose_name='Рекомендуемая можность БП, Вт')
    image = models.ImageField(null=True, verbose_name='Изображение')
    computer_id = models.ManyToManyField(DeletedComputer, related_name='related_GPU', blank=True)

    class Meta:
        verbose_name = 'DeletedGPU'


class DeletedCPU(models.Model):
    manufacturer = models.TextField(max_length=50, verbose_name='Изготовитель')
    cpu_series = models.TextField(max_length=50, verbose_name='Серия')
    threads = models.PositiveIntegerField(verbose_name='Количество потоков')
    cpu_speed = models.PositiveIntegerField(verbose_name='Частота, МГц')
    cpu_cores = models.PositiveIntegerField(verbose_name='Количество ядер')
    cpu_socket = models.TextField(max_length=50, verbose_name='Сокет')
    cpu_turbo_speed = models.PositiveIntegerField(verbose_name='Максимальная тактовая частота, МГц')
    l3_Cache = models.PositiveIntegerField(verbose_name='Кэш, Мб')
    unlocked_multiplier = models.BooleanField(verbose_name='Возможность для разгона')
    release_year = models.PositiveIntegerField(verbose_name='Год релиза')
    image = models.ImageField(null=True, verbose_name='Изображение')
    computer_id = models.ManyToManyField(DeletedComputer, related_name='related_CPU', blank=True)

    class Meta:
        verbose_name = 'DeletedCPU'


class DeletedHDD(models.Model):
    model = models.TextField(max_length=50, verbose_name='Модель')
    manufacturer = models.TextField(max_length=50, verbose_name='Изготовитель')
    cache = models.PositiveIntegerField(verbose_name='Кэш, Мб')
    spindle_speed = models.PositiveIntegerField(verbose_name='Скорость винта, обр/мин')
    interface_type = models.TextField(max_length=50, verbose_name='Тип интерфейса')
    capacity = models.PositiveIntegerField(verbose_name='Емкость, Тб')
    form_factor = models.TextField(max_length=50, verbose_name='Форм-фактор')
    release_year = models.PositiveIntegerField(verbose_name='Год релиза')
    computer_id = models.ManyToManyField(DeletedComputer, related_name='related_HDD', blank=True)
    image = models.ImageField(null=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'DeletedHDD'


class DeletedRAM(models.Model):
    model = models.TextField(max_length=50, verbose_name='Модель')
    manufacturer = models.TextField(max_length=50, verbose_name='Изготовитель')
    ram_technology = models.TextField(max_length=50, verbose_name='Технология')
    ram_speed = models.PositiveIntegerField(verbose_name='Частота памяти, МГц')
    capacity = models.PositiveIntegerField(verbose_name='Емкость, Гб')
    number_of_modules = models.PositiveIntegerField(verbose_name='Количество модулей')
    release_year = models.PositiveIntegerField(verbose_name='Год релиза')
    computer_id = models.ManyToManyField(DeletedComputer, related_name='related_RAM', blank=True)
    image = models.ImageField(null=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'DeletedRAM'


class DeletedCase(models.Model):
    manufacturer = models.TextField(max_length=50, verbose_name='Изготовитель')
    model = models.TextField(max_length=50, verbose_name='Модель')
    color = models.TextField(max_length=50, verbose_name='Цвет')
    form_factor = models.TextField(max_length=50, verbose_name='Форм-фактор')
    material = models.TextField(max_length=50, verbose_name='Материал')
    height = models.PositiveIntegerField(verbose_name='Высота, мм')
    width = models.PositiveIntegerField(verbose_name='Ширина, мм')
    depth = models.PositiveIntegerField(verbose_name='Глубина, мм')
    max_size_of_motherboard = models.TextField(verbose_name='Максимальный размер материнской платы')
    release_year = models.PositiveIntegerField(verbose_name='Год релиза')
    computer_id = models.ManyToManyField(DeletedComputer, related_name='related_Case', blank=True)
    image = models.ImageField(null=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'DeletedCase'


class DeletedPowerBlock(models.Model):
    manufacturer = models.TextField(max_length=50, verbose_name='Изготовитель')
    model = models.TextField(max_length=50, verbose_name='Модель')
    power = models.PositiveIntegerField(verbose_name='Мощность, Вт')
    form_factor = models.TextField(max_length=50, verbose_name='Форм-фактор')
    kpd = models.PositiveIntegerField(verbose_name='КПД, %')
    motherboard_power = models.TextField(max_length=50, verbose_name='Питание платы')
    release_year = models.PositiveIntegerField(verbose_name='Год релиза')
    computer_id = models.ManyToManyField(DeletedComputer, related_name='related_PowerBlock', blank=True)
    image = models.ImageField(null=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'DeletedPowerBlock'


class DeletedMotherBoard(models.Model):
    manufacturer = models.TextField(max_length=50, verbose_name='Изготовитель')
    model = models.TextField(max_length=50, verbose_name='Модель')
    ram_type = models.TextField(max_length=50, verbose_name='Тип памяти')
    form_factor = models.TextField(max_length=50, verbose_name='Форм-фактор')
    amount_of_slots_for_ram = models.PositiveIntegerField(verbose_name='Количество слотов памяти')
    socket = models.TextField(max_length=50, verbose_name="Сокет")
    amount_of_usb = models.PositiveIntegerField(verbose_name='Количество портов USB', blank=True, null=True)
    amount_of_hdmi = models.PositiveIntegerField(verbose_name='Количество портов HDMI', blank=True, null=True)
    amount_of_displayport = models.PositiveIntegerField(verbose_name='Количество портов DisplayPort', blank=True,
                                                        null=True)
    amount_of_vga = models.PositiveIntegerField(verbose_name='Количество портов VGA', blank=True, null=True)
    max_speed_of_ram = models.PositiveIntegerField(verbose_name='Максимальная частота памяти, МГц')
    release_year = models.PositiveIntegerField(verbose_name='Год релиза')
    computer_id = models.ManyToManyField(DeletedComputer, related_name='related_MotherBoard', blank=True)
    image = models.ImageField(null=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'DeletedMotherBoard'

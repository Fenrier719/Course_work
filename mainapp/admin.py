from django.contrib import admin
from .models import *

admin.site.register(Computer)
admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(MotherBoard)
admin.site.register(HDD)
admin.site.register(RAM)
admin.site.register(Case)
admin.site.register(PowerBlock)
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.apps import apps
from django.contrib.sessions.models import Session

from .models import *


def show(request):
    return render(request, 'mainapp/base.html')


class CPUDetailView(DetailView):
    model = CPU
    pk_url_kwarg = 'id'


def cpu_list(request):
    cpu = CPU.objects.all()
    manufacturers = cpu.distinct('manufacturer')
    model = cpu.distinct('CPU_series')
    search_query = request.GET.getlist('manufacturer', '')
    if search_query:
        cpu = CPU.objects.filter(manufacturer__in=search_query)
    return render(request, 'mainapp/cpu_list.html', {'cpus': cpu, 'mans': manufacturers, 'models': model})


class GPUDetailView(DetailView):
    model = GPU
    pk_url_kwarg = 'id'


def gpu_list(request):
    gpu = GPU.objects.all()
    manufacturers = gpu.distinct('manufacturer')
    model = gpu.distinct('chipset')
    search_query = request.GET.getlist('manufacturer', '')
    if search_query:
        gpu = GPU.objects.filter(manufacturer__in=search_query)
    return render(request, 'mainapp/gpu_list.html', {'gpus': gpu, 'mans': manufacturers, 'models': model})


class RAMDetailView(DetailView):
    model = RAM
    pk_url_kwarg = 'id'


def ram_list(request):
    ram = RAM.objects.all()
    manufacturers = ram.distinct('manufacturer')
    model = ram.distinct('models')
    search_query = request.GET.getlist('manufacturer', '')
    if search_query:
        ram = RAM.objects.filter(manufacturer__in=search_query)
    return render(request, 'mainapp/ram_list.html', {'rams': ram, 'mans': manufacturers, 'models': model})


class PowerUnitDetailView(DetailView):
    model = PowerBlock
    pk_url_kwarg = 'id'


def powerunit_list(request):
    powerunit = PowerBlock.objects.all()
    manufacturers = powerunit.distinct('manufacturer')
    model = powerunit.distinct('models')
    search_query = request.GET.getlist('manufacturer', '')
    if search_query:
        powerunit = PowerBlock.objects.filter(manufacturer__in=search_query)
    return render(request, 'mainapp/powerunit_list.html',
                  {'powerunits': powerunit, 'mans': manufacturers, 'models': model})


class CaseDetailView(DetailView):
    model = Case
    pk_url_kwarg = 'id'


def case_list(request):
    case = Case.objects.all()
    manufacturers = case.distinct('manufacturer')
    model = case.distinct('models')
    search_query = request.GET.getlist('manufacturer', '')
    if search_query:
        case = Case.objects.filter(manufacturer__in=request.GET.getlist('manufacturer'))
    return render(request, 'mainapp/case_list.html', {'cases': case, 'mans': manufacturers, 'models': model})


class PCDetailView(DetailView):
    model = Computer
    pk_url_kwarg = 'id'


def pc_list(request):
    pc = Computer.objects.all()
    manufacturers = pc.distinct('manufacturer')
    search_query = request.GET.getlist('manufacturer', '')
    if search_query:
        pc = Computer.objects.filter(manufacturer__in=search_query)
    return render(request, 'mainapp/pc_list.html', {'pcs': pc, 'mans': manufacturers, 'models': model})


class HDDDetailView(DetailView):
    model = HDD
    pk_url_kwarg = 'id'


def hdd_list(request):
    hdd = HDD.objects.all()
    manufacturers = hdd.distinct('manufacturer')
    model = hdd.distinct('models')
    search_query = request.GET.getlist('manufacturer', '')
    if search_query:
        hdd = HDD.objects.filter(manufacturer__in=request.GET.getlist('manufacturer'))
    return render(request, 'mainapp/hdd_list.html', {'hdds': hdd, 'mans': manufacturers, 'models': model})


class MotherBoardDetailView(DetailView):
    model = MotherBoard
    pk_url_kwarg = 'id'


def motherboard_list(request):
    motherboard = MotherBoard.objects.all()
    manufacturers = motherboard.distinct('manufacturer')
    model = motherboard.distinct('models')
    search_query = request.GET.getlist('manufacturer', '')
    if search_query:
        motherboard = MotherBoard.objects.filter(manufacturer__in=request.GET.getlist('manufacturer'))
    return render(request, 'mainapp/motherboard_list.html',
                  {'motherboards': motherboard, 'mans': manufacturers, 'models': model})


def add_to_comparison(request, id):
    product = request.GET.get('product', '')
    if request.session.get('first_item', False):
        request.session['second_item'] = id
        request.session['second_item_product'] = product
        redirect('http://127.0.0.1:8000/comparison/')
    else:
        request.session['first_item'] = id
        request.session['first_item_product'] = product
    return redirect(request.META.get('HTTP_REFERER'))


def comparison_view(request):
    first_item_id = request.session.get('first_item')
    second_item_id = request.session.get('second_item')

    if first_item_id is None or second_item_id is None:
        return HttpResponse('<h1>У вас нет комплектующих для сравнения</h1>')

    product = request.session.get('first_item_product')
    model = apps.get_model('mainapp', product.title())
    first_item = model.objects.get(id=int(first_item_id))
    second_item = model.objects.get(id=int(second_item_id))


    data = {
        'first_item': first_item,
        'second_item': second_item,
        'fields': list(map(lambda field: field.name, model._meta.get_fields()))[
                  1:len(list(map(lambda field: field.name, model._meta.get_fields()))) - 2:],

    }
    return render(request, 'mainapp/comparator.html', data)


def clear_comparator(request):
    request.session.modified = True
    del request.session['first_item']
    del request.session['second_item']
    return redirect('http://127.0.0.1:8000/general/')

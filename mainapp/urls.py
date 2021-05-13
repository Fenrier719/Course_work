from django.urls import path, include
from .views import *

urlpatterns = [
    path('general/', show),
    path('cases/', case_list, name='case_list'),
    path('cpus/', cpu_list, name='cpu_list'),
    path('gpus/', gpu_list, name='gpu_list'),
    path('motherboards/', motherboard_list, name='motherboard_list'),
    path('powerunits/', powerunit_list, name='powerunit_list'),
    path('pcs/', pc_list),
    path('rams/', ram_list, name='ram_list'),
    path('hdds/', hdd_list, name='hdd_list'),
    path('cpus/<int:id>/', CPUDetailView.as_view()),
    path('cases/<int:id>/', CaseDetailView.as_view()),
    path('gpus/<int:id>/', GPUDetailView.as_view()),
    path('hdds/<int:id>/', HDDDetailView.as_view()),
    path('motherboards/<int:id>/', MotherBoardDetailView.as_view()),
    path('powerunits/<int:id>/', PowerUnitDetailView.as_view()),
    path('pcs/<int:id>/', PCDetailView.as_view()),
    path('rams/<int:id>/', RAMDetailView.as_view()),
    path('add_to_comp/<int:id>', add_to_comparison, name='add_to_comp'),
    path('compare/', comparison_view, name='compare'),
    path('clear_comparator/', clear_comparator, name='clear')
]

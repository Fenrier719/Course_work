from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from .views import *
from . import views


urlpatterns = [
    url(r'dialogs/$', login_required(views.DialogsView.as_view()), name='dialogs'),
    path(r'dialogs/create/<int:user_id>/', login_required(views.CreateDialogView.as_view()), name='create_dialog'),
    url(r'dialogs/(?P<chat_id>\d+)/$', login_required(views.MessagesView.as_view()), name='messages'),
    path('all_users/', UsersListView.as_view(), name='get_users')
]

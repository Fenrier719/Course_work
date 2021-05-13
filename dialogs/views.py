from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View, generic

from dialogs.forms import MessageForm
from .models import Dialog


class UsersListView(generic.ListView):
    queryset = User.objects.all()
    template_name = 'users/all_users.html'
    context_object_name = 'users'


class DialogsView(View):
    def get(self, request):
        chats = Dialog.objects.filter(members__in=[request.user.id])
        return render(request, 'users/dialogs.html', {'user_profile': request.user, 'chats': chats})


class MessagesView(View):
    def get(self, request, chat_id):
        chat = Dialog.objects.get(id=chat_id)

        return render(
            request,
            'users/messages.html',
            {
                'user_profile': request.user,
                'chat': chat,
                'form': MessageForm()
            }
        )

    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('messages', kwargs={'chat_id': chat_id}))


class CreateDialogView(View):
    def get(self, request, user_id):
        chats = Dialog.objects.filter(members__in=[request.user.id, user_id]).annotate(
            c=Count('members')).filter(c=2)
        if chats.count() == 0:
            chat = Dialog.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        return redirect(reverse('messages', kwargs={'chat_id': chat.id}))

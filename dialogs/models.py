from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Dialog(models.Model):
    members = models.ManyToManyField(User, verbose_name=_("Участник"))

    def get_absolute_url(self):
        return reverse('messages', kwargs={'chat_id': self.pk})

    def __str__(self):
        return f'Диалог между {" и ".join(member.username for member in self.members.all())}'


class Message(models.Model):
    chat = models.ForeignKey(Dialog, verbose_name=_("Диалог"), on_delete=models.CASCADE)
    author = models.ForeignKey(User, default='', verbose_name=_("Пользователь"), on_delete=models.CASCADE)
    message = models.TextField(_("Сообщение"))
    pub_date = models.DateTimeField(_('Дата сообщения'), default=timezone.now)
    is_read = models.BooleanField(_('Прочитано'), default=False)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message

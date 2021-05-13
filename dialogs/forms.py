from django.forms import ModelForm

from dialogs.models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ""}
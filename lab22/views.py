from django.db import connection
from django.shortcuts import render

from lab22 import forms


def execprocedure(request, username):
    c = connection.cursor()
    try:
        c.callproc("getid", (username,))
        data = c.fetchall()
    finally:
        c.close()
    return render(request, 'BD/lab22.html', data)


def execprocedure(request):
    c = connection.cursor()
    r = ''
    if request.method == 'POST':
        form = forms.FirstForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data.get('username')
                c.callproc('getid', (username,))
                r = c.fetchall()
                return render(request, 'BD/lab22.html', {'result': r})
            finally:
                c.close()
    else:
        form = forms.FirstForm()
    return render(request, 'BD/lab22.html', {'result': r, 'form': form})


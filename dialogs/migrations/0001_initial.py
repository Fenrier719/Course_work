# Generated by Django 3.2 on 2021-05-09 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Участник')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата сообщения')),
                ('is_read', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dialogs.dialog', verbose_name='Диалог')),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
    ]

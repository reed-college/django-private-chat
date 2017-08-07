from django.contrib import admin
from django.conf import settings
from .models import Dialog, Message


class DialogAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'modified', 'owner', 'opponent')
    list_filter = ('created', 'modified', 'owner', 'opponent')



class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'is_removed',
        'dialog',
        'sender',
        'text',
    )
    list_filter = ('created', 'modified', 'is_removed', 'dialog', 'sender')

if settings.DEBUG:
    admin.site.register(Dialog, DialogAdmin)
    admin.site.register(Message, MessageAdmin)

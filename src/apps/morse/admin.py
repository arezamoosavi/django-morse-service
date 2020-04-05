from django.contrib import admin
from .models import ReceiveSentence, MorseCombination

class ReceiveSentenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'sentence', 'receive_date')
    list_display_links = ('id', 'sentence', 'receive_date')

admin.site.register(ReceiveSentence, ReceiveSentenceAdmin)

class MorseCombinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'combination')
    list_display_links = ('id', 'word', 'combination')

admin.site.register(MorseCombination, MorseCombinationAdmin)

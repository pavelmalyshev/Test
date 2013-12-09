from django.contrib import admin
from note.models import Autor
from note.models import Stat

class StatAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
class AutorAdmin(admin.ModelAdmin):
    search_fields = ['fio']

admin.site.register(Autor, AutorAdmin)
admin.site.register(Stat, StatAdmin)
# Register your models here.

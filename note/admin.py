from django.contrib import admin
from note.models import Autor, Stat, Comment


class StatAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
class AutorAdmin(admin.ModelAdmin):
    search_fields = ['fio']

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['who']
        

admin.site.register(Autor, AutorAdmin)
admin.site.register(Stat, StatAdmin)
admin.site.register(Comment, CommentAdmin)
# Register your models here.

from django.contrib import admin
from . import models as NewsModels

# Register your models here.
class AdminNews(admin.ModelAdmin):
    list_display = ['headlines', 'reportedBy','addedDate','description']
admin.site.register(NewsModels.News, AdminNews)
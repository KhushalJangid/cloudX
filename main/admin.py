from django.contrib import admin
from main.models import Data
# from import_export.admin import ImportExportModelAdmin
# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ["id","title","user","type","date"]
    search_fields = ["title","type","date"]
    # readonly_fields = ["date_joined","last_login"]
       
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering =()

admin.site.register(Data,DataAdmin)
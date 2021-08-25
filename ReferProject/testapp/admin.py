from django.contrib import admin
from django.db.models.query_utils import select_related_descend
from . models import Apps

class AppAdmin(admin.ModelAdmin):
    list_display=['no','appname','logo','category','description','andriod_link','andriod_rate','ios_link','ios_rate','publish']
    list_filter=('appname','publish')
    search_fields=('appname','description')
    prepopulated_fields={'slug':('appname',)}

# Register your models here.
admin.site.register(Apps,AppAdmin)
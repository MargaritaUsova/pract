from django.contrib import admin

# Register your models here.
from .models import Task

admin.site.register(Task)
from django.contrib import admin
from .models import Task


# Register your models here.
admin.site.unregister(Task)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('nameTranslit', 'price', 'name', 'cashback',
                    'screen', 'brand', 'proc', 'rom',  'camera', 'cur_price',
                    'previous_price',)
    prepopulated_fields = {"slug": ("nameTranslit", 'name')}


admin.site.register(Task, MemberAdmin)
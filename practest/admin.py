from django.contrib import admin
from .models import Person

@admin.register(Person)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'phone', 'address', 'gender')

# Register your models here.

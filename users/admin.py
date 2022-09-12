from django.contrib import admin
from .models import Client, Employee, Visit, Procedure

admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Procedure)
admin.site.register(Visit)
from django.contrib import admin

# Register your models here.

from models import Theme, Trip

admin.site.register([Theme, Trip])

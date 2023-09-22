from django.contrib import admin
from .models import Funko, Buyer, Admirer

# Register your models here.
admin.site.register(Funko)
admin.site.register(Buyer)
admin.site.register(Admirer)
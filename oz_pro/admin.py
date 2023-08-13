from django.contrib import admin
from .models import Customer, ServicePackage, Event, Lead

# Register your models here.
admin.site.register(Customer)
admin.site.register(ServicePackage)
admin.site.register(Event)
admin.site.register(Lead)
from django.db import models

# Create your models here.

class Lead(models.Model):
    image = models.ImageField(upload_to='static/pics', default = 'Picture7.png')
    ID = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=255,null=False)
    phone_number = models.CharField(max_length=15,null=False)
    event_type = models.TextField()
    event_date = models.DateField(null=False)
    date_of_creation = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name}, {self.ID}'
    
class Customer(models.Model):
    image = models.ImageField(upload_to='static/pics', default = 'Picture7.png')
    ID = models.PositiveIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    customer_type = models.CharField(max_length=50)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Customer Name: {self.name}\nID: {self.ID}\nPhone Number: {self.phone_number}\nType:: {self.customer_type}"

class ServicePackage(models.Model):
    image = models.ImageField(upload_to='static/pics', default = 'pack.png')
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    package_details = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    image = models.ImageField(upload_to='static/pics', default = 'event.png')
    ID = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True, related_name='events_for_customer')
    service_package = models.ForeignKey(ServicePackage, on_delete=models.SET_NULL, null=True, related_name='events_for_service_package')
    name = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    number_of_attendees = models.PositiveIntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.ID}\nCustomer ID: {self.customer}\nService package ID: {self.service_package}"

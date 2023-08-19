from datetime import datetime
from django.http import HttpResponse, request
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from oz_pro.models import Customer, Lead, Event, ServicePackage

# pages rendering functions bellow:
def welcome_page(request):
    print("********* Welcome page function **********")
    return render(request, 'welcome.html')

@login_required
def leads_page(request):
    print("********* After agent login -- home page function *********")    
    all_leads = Lead.objects.all()
    context = {
        'leads': all_leads
    }
    return render(request, 'leads.html', context)

def customers_page(request):
    print("********* Customer page functio n*********")
    all_customers = Customer.objects.all()
    context = {
        'customers': all_customers
    }
    return render(request, 'customers.html', context)

def events_page(request):
    print("********* Event page function *********")
    all_events = Event.objects.all()
    context = {
        'events': all_events
    }
    return render(request, 'events.html', context)

def service_packages_page(request):
    print("********* Service package page function *********")
    all_service_packages = ServicePackage.objects.all()
    context = {
        'service_packages': all_service_packages
    }
    return render(request, 'service_packages.html', context)


# Lead fuctions bellow:
def create_lead(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        tel = request.POST.get('tel')
        eventType = request.POST.get('eventType')
        date = request.POST.get('date')
        try:
            new_lead = Lead(name=username,phone_number=tel,event_type=eventType, event_date=date) 
            new_lead.save()
            messages.error(request, "Your details have been submitted! We will be in touch soon.")
        except:
            messages.error(request, "An error occurred. Please enter check date value entered correctlly.")
    
    return redirect('welcome')

def delete_lead(request, lead_id):
    print("********* Delete lead function *********")
    lead = Lead.objects.get(pk=lead_id)
    lead.delete()
    return redirect('all_leads')


# Customer fuctions bellow:
def add_customer(request):   
    print("********* Add customer function*********") 
    if request.method == 'POST':
        id = request.POST.get('addID')
        name = request.POST.get('addName')
        tel = request.POST.get('addTel')
        cust_type = request.POST.get('addType')
        try:
            new_customer = Customer(ID=id, name=name, phone_number=tel, customer_type=cust_type) 
            new_customer.save()
            messages.error(request, f"Customer created successfully: {str(new_customer)} !")
        except IntegrityError: 
             messages.error(request, f"Customer with ID {id} already exists.")
        except ValueError:
            messages.error(request, "An error occurred. Please check the values you entered.")
    
    return redirect('all_customers')
    
def update_customer(request, customer_id):
    print("********* Update customer function *********")
    if request.method == "POST":
        customer = Customer.objects.get(pk=customer_id)
        
        # Check if user has provided phone number, if not, don't update it
        update_tel = request.POST.get('updateTel')
        if update_tel:  # if not empty or None
            customer.phone_number = update_tel
            
        # Check if user has provided customer type, if not, don't update it
        update_type = request.POST.get('updateType')
        if update_type:  # if not empty or None
            customer.customer_type = update_type
        
        customer.save()    
    return redirect('all_customers')


# Event fuctions bellow:
def add_event(request):   
    print("********* Add event function*********") 
    if request.method == 'POST':

        cust_id = request.POST.get('addCustomerID')
        pack_id = request.POST.get('addServicePackageID')
        name = request.POST.get('addName')
        ven = request.POST.get('addVenue')
        attend = request.POST.get('addAttendees')
        bud = request.POST.get('addBudget')
       
        try:
            chek_cust_id = Customer.objects.get(ID=cust_id)
            chek_pack_id = ServicePackage.objects.get(ID=pack_id)
            
            
            new_event = Event(customer=chek_cust_id, service_package=chek_pack_id ,name=name, venue=ven, number_of_attendees=attend, budget=bud) 
            new_event.save()
            
        except Customer.DoesNotExist:
            messages.error(request, f"Customer with ID {cust_id} does not exist.")
        except ServicePackage.DoesNotExist:
            messages.error(request, f"Service Package with ID {pack_id} does not exist.")
        except ValueError as e:
            print("Error: ", str(e))
            messages.error(request, "An error occurred. Please check the values you entered.")
    
    return redirect('all_events')
    
def update_event(request, event_id):
    print("********* Update event function *********")
    if request.method == "POST":
        event = Event.objects.get(pk=event_id)
        
        # Check if user has provided phone number, if not, don't update it
        update_name = request.POST.get('updateName')
        if update_name:  # if not empty or None
            event.name = update_name
            
        # Check if user has provided event type, if not, don't update it
        update_venue = request.POST.get('updateVenue')
        if update_venue:  # if not empty or None
            event.venue = update_venue
            
        # Check if user has provided event type, if not, don't update it
        update_attendees = request.POST.get('updateAttendees')
        if update_attendees:  # if not empty or None
            event.number_of_attendees = update_attendees
            
        # Check if user has provided event type, if not, don't update it
        update_budget = request.POST.get('updateBudget')
        if update_budget:  # if not empty or None
            event.budget = update_budget
            
      
        event.save()    
    return redirect('all_events')

# servicepackage fuctions bellow:
def add_service_package(request):   
    print("********* Add Service Package function*********") 
    if request.method == 'POST':
        name = request.POST.get('addName')
        deats = request.POST.get('addDeats')
        try:
            new_service_package = ServicePackage(name=name, package_details=deats) 
            new_service_package.save()
      
        except:
            messages.error(request, "An error occurred. Please check the values you entered.")
    
    return redirect('all_service_packages')

def update_service_package(request, service_package_id):
    print("********* Update service package function *********")
    if request.method == "POST":
        service_package = ServicePackage.objects.get(pk=service_package_id)
        
        # Check if user has provided phone number, if not, don't update it
        update_details = request.POST.get('updateDetails')
        if update_details:  # if not empty or None
            service_package.package_details = update_details
            
        service_package.save()    
    return redirect('all_service_packages')












# def display_events_of_customer(request):
#     print("********* All events of customer function *********")
#     events_cust_id = request.GET.get(events_cust_id)
#     all_events = Event.object.all()
#     if events_cust_id:
#         all_events = all_events.filter(customer__exact=events_cust_id)
#         context = {
#             'events': all_events
#         }
#     return render(request, 'events.html', context)
# TODO: implentation in the events.html file in the table: href={% url 'all_events'%}?events_cust_id={{event.custotomer}},  
#  also to check if i can do it on time.



# agent login and logut functions bellow:
def agent_login(request):
    print("********* Agent-login function *********")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Successful authentication
            login(request, user)
            return redirect('all_leads')
        else:
            # Invalid credentials, show an error message or handle as needed.
            messages.error(request, "An error occurred. USER NOT EXIST!.")
            return render(request, 'welcome.html')
    return render(request, 'leads.html')

def agent_logout(request):
    print("*********Agent-logout function*********")
    logout(request)
    return redirect('welcome')








   
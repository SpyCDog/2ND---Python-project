from datetime import datetime
from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from oz_pro.models import Customer, Lead, Event, ServicePackage

# pages rendering functions bellow:
def welcome_page(request):
    print("********* dropPage -- welcome page function**********")
    return render(request, 'welcome.html')

@login_required
def leads_page(request):
    print("*********after agent login -- home page function*********")    
    all_leads = Lead.objects.all()
    context = {
        'leads': all_leads
    }
    return render(request, 'leads.html', context)

def customers_page(request):
    print("*********customer page function*********")
    all_customers = Customer.objects.all()
    context = {
        'customers': all_customers
    }
    return render(request, 'customers.html', context)

def events_page(request):
    print("*********event page function*********")
    all_events = Event.objects.all()
    context = {
        'events': all_events
    }
    return render(request, 'events.html', context)

def service_packages_page(request):
    print("*********service package page function*********")
    all_service_packages = ServicePackage.objects.all()
    context = {
        'service_packages': all_service_packages
    }
    return render(request, 'service_packages.html', context)

# lead fuctions bellow:
def create_lead(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        tel = request.POST.get('tel')
        eventType = request.POST.get('eventType')
        date = request.POST.get('date')
        new_lead = Lead(name=username,phone_number=tel,event_type=eventType, event_date=date) 
        new_lead.save()
        return redirect('welcome') 
    
    return render(request, 'welcome.html')


def delete_lead(request, lead_id):
    print("*********delete lead function*********")
    lead = Lead.objects.get(pk=lead_id)
    lead.delete()
    return redirect('all_leads')


# customer fuctions bellow:

# def update_lead(request, customer_id):
#     if request.method == 'POST':
#         tel = request.POST.get('tel')
#         eventType = request.POST.get('eventType')
#         date = request.POST.get('date')
#         new_lead = Lead(name=username,phone_number=tel,event_type=eventType, event_date=date) 
#         new_lead.save()
#         return redirect('welcome') 
    
#     return render(request, 'welcome.html')



def display_events_of_customer(request):
    print("*********all events of customer function*********")
    events_cust_id = request.GET.get(events_cust_id)
    all_events = Event.object.all()
    if events_cust_id:
        all_events = all_events.filter(customer__exact=events_cust_id)
        context = {
            'events': all_events
        }
    return render(request, 'events.html', context)
# TODO: implentation in the events.html file in the table: href={% url 'all_events'%}?events_cust_id={{event.custotomer}}



# agent login and logut functions bellow:
def agent_login(request):
    print("*********agent login function*********")
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
            return render(request, 'welcome.html', {'error': 'Invalid credentials'})
    return render(request, 'leads.html')

def agent_logout(request):
    print("*********agent logout function*********")
    logout(request)
    return redirect('welcome')








   
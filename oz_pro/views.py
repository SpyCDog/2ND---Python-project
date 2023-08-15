from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from oz_pro.models import Customer, Lead, Event
from .forms import LeadForm

# Create your views here.
# def customers_page(request):
#     all_customers = Customer.objects.all()
#     return HttpResponse(f"This is the customers: {all_customers}")

# def customers_page(request):
#     all_customers = Customer.objects.all()
#     context = {
#         'customers': all_customers 
#     }
#    return render(request, 'welcome,html')



# def create_lead(request):
#     if request.method == 'POST':
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('welcome')  # replace 'some_view_name' with the name of the view to redirect to
#     else:
#         form = LeadForm()
#     return render(request, 'welcome.html', {'form': form})

   
def customers_page(request):
    print("*********customer page function*********")
    all_customers = Customer.objects.all()
    context = {
        'customers': all_customers
    }
    return render(request, 'customers.html', context)


def home_page(request):
    print("*********after agent login -- home page function*********")    
    all_leads = Lead.objects.all()
    context = {
        'leads': all_leads
    }
    return render(request, 'home1.html', context)

def delete_lead(request, lead_id):
    print("*********delete lead function*********")
    lead = Lead.objects.get(pk=lead_id)
    lead.delete()
    return redirect('all_leads')


def welcome_page(request):
    print("********* dropPage -- welcome page function**********")
    return render(request, 'welcome.html')

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
    return render(request, 'home1.html')

def agent_logout(request):
    print("*********agent logout function*********")
    logout(request)
    return redirect('welcome')






   
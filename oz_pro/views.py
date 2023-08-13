from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from oz_pro.models import Customer, Lead
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
    all_customers = Customer.objects.all()
    context = {
        'customers': all_customers
    }
    return render(request, 'customers.html', context)


def home_page(request):
    all_leads = Lead.objects.all()
    context = {
        'leads': all_leads
    }
    return render(request, 'home1.html', context)

def delete_lead(request, lead_id):
    lead = Lead.objects.get(pk=lead_id)
    lead.delete()
    return redirect('all_leads')


def welcome_page(request):

    return render(request, 'welcome.html')


# def login_page(request):

#     return render(request, 'agent_login.html')



   
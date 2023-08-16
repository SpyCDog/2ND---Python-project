from django.urls import path
from oz_pro import views

urlpatterns = [
    path('', views.welcome_page, name='welcome'),
    path('leads/', views.leads_page, name='all_leads'),
    path('create_leads/', views.create_lead, name='create_lead'),
    path('customers/', views.customers_page, name='all_customers'),
    path('events/', views.events_page, name='all_events'),
    path('service_packages/', views.service_packages_page, name='all_service_packages'),
    path('login', views.agent_login, name='agent_login'),
    path('logout', views.agent_logout, name='agent_logout'),
    path('delete_lead/<int:lead_id>/', views.delete_lead, name='delete_lead'),
    
    
]

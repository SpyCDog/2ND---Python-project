from django.urls import path
from oz_pro import views

urlpatterns = [
    path('', views.welcome_page, name='welcome'),
    path('leads/', views.leads_page, name='all_leads'),
    path('customers/', views.customers_page, name='all_customers'),
    path('events/', views.events_page, name='all_events'),
    path('service_packages/', views.service_packages_page, name='all_service_packages'),
    path('login', views.agent_login, name='agent_login'),
    path('logout', views.agent_logout, name='agent_logout'),
    
    
    path('create_leads/', views.create_lead, name='create_lead'),
    path('delete_lead/<int:lead_id>/', views.delete_lead, name='delete_lead'),
    
    path('add_customer/', views.add_customer, name='add_customer'),
    path('update_customer/<int:customer_id>/', views.update_customer, name='update_customer'),
    
    path('add_event/', views.add_event, name='add_event'),
    path('update_event/<int:event_id>/', views.update_event, name='update_event'),

    
    path('add_service_package/', views.add_service_package, name='add_service_package'),
    path('update_service_package/<int:service_package_id>/', views.update_service_package, name='update_service_package'),
    
    
]

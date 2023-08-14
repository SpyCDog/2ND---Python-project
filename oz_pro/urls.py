from django.urls import path
from oz_pro import views

urlpatterns = [
    path('', views.welcome_page, name='welcome'),
    path('login', views.agent_login, name='agent_login'),
    path('home/', views.home_page, name='all_leads'),
    path('delete_lead/<int:lead_id>/', views.delete_lead, name='delete_lead'),
    path('customers/', views.customers_page, name='all_customers'),
    path('events/', views.customers_page, name='all_events'),
    path('service packages/', views.customers_page, name='all_service_packages'),
    path('Customers/', views.customers_page, name='all_customers'),
    
    # path('home/', views.home_page_page, name='home_all_leads'),
    
]

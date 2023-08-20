from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Customer, Lead, ServicePackage, Event
# Create your tests here.


class WelcomePageTests(TestCase):

    def test_welcome_page(self):
        response = self.client.get(reverse('welcome_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome.html')

class LeadTests(TestCase):

    def setUp(self):
        # Create a test lead
        self.lead = Lead.objects.create(name="Test Lead", phone_number="1234567890", event_type="Test Event", event_date="2023-08-20")
        
    def test_all_leads(self):
        response = self.client.get(reverse('all_leads'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leads.html')
        
    # You can continue adding more test methods for other Lead functionalities like create_lead, delete_lead etc.

# Continue with similar structure for CustomerTests, EventTests, ServicePackageTests, and so on.




class LeadAuthTests(TestCase):

    def setUp(self):
        # Create a test user and log them in
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.lead = Lead.objects.create(name="Test Lead", phone_number="1234567890", event_type="Test Event", event_date="2023-08-20")
        
    def test_leads_page_authenticated(self):
        response = self.client.get(reverse('all_leads'))
        self.assertEqual(response.status_code, 200)

    def test_leads_page_unauthenticated(self):
        self.client.logout()  # log the user out
        response = self.client.get(reverse('all_leads'))
        self.assertNotEqual(response.status_code, 200)  # Expect a redirect or some other response code


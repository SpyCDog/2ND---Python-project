from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Customer, Lead, ServicePackage, Event
# Create your tests here.


class LeadModelTest(TestCase):

    def setUp(self):
        self.lead = Lead.objects.create(
            name="Test Lead",
            phone_number="123456789",
            event_type="Wedding",
            event_date="2023-08-18"
        )

    def test_lead_creation(self):
        self.assertTrue(isinstance(self.lead, Lead))
        self.assertEqual(self.lead.name, 'Test Lead')
        
    def test_lead_deletion(self):
        self.lead.delete()
        
        with self.assertRaises(Lead.DoesNotExist):
            deleted_lead = Lead.objects.get(pk=self.lead.ID)

class CustomerModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            ID=1,
            name="Test Customer",
            phone_number="123456789",
            customer_type="Regular"
        )

    def test_customer_creation(self):
        self.assertTrue(isinstance(self.customer, Customer))
        self.assertEqual(self.customer.name, 'Test Customer')
        
        
    def test_customer_update(self):
            # Update the customer's name
            self.customer.name = "Updated Customer"
            self.customer.save()

            # Retrieve the customer from the database again
            updated_customer = Customer.objects.get(ID=1)
            
            # Check if the update worked
            self.assertEqual(updated_customer.name, "Updated Customer")
            

class EventViewTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            ID=1,
            name="Test Customer",
            phone_number="123456789",
            customer_type="Regular"
        )
        self.service_package = ServicePackage.objects.create(
            name="Gold Package",
            package_details="Details about gold package."
        )
        self.event = Event.objects.create(
            customer=self.customer,
            service_package=self.service_package,
            name="Test Event",
            venue="Test Venue",
            number_of_attendees=100,
            budget=1000.00
        )

    def test_event_creation(self):
        self.assertTrue(isinstance(self.event, Event))
        self.assertEqual(self.event.name, 'Test Event')

    def test_event_view(self):
        resp = self.client.get(reverse('all_events'))  # Assuming 'all_events' is the name of your events_page url pattern
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.event, resp.context['events'])
        
    def test_event_update_view(self):
        # Assuming you use a POST method to update an event and the URL takes in the event's ID
        update_url = reverse('update_event', args=[self.event.ID])
        
        # Data to update
        updated_data = {
            'name': 'Updated Event Name',
            'venue': 'Updated Venue',
            'number_of_attendees': 200,
            'budget': 1500.00
        }
        
        resp = self.client.post(update_url, updated_data)
        
        # Assuming a successful update redirects to the 'all_events' page
        self.assertEqual(resp.status_code, 302)

        # Fetch the event again from the database
        updated_event = Event.objects.get(ID=self.event.ID)
        
        # Check if the data was updated
        self.assertEqual(updated_event.name, 'Updated Event Name')
        self.assertEqual(updated_event.venue, 'Updated Venue')
        self.assertEqual(updated_event.number_of_attendees, 200)
        self.assertEqual(updated_event.budget, 1500.00)


class AgentLoginTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_correct_login(self):
        resp = self.client.post(reverse('agent_login'), {'username': 'testuser', 'password': '12345'})  # Assuming 'agent_login' is the name of your agent_login url pattern
        self.assertEqual(resp.status_code, 302)  # Expecting a redirect
        self.assertTrue(resp.context['user'].is_authenticated)

    def test_wrong_login(self):
        resp = self.client.post(reverse('agent_login'), {'username': 'wronguser', 'password': 'wrongpass'})
        self.assertEqual(resp.status_code, 200)  # Stays on the same page
        self.assertFalse(resp.context['user'].is_authenticated)

# Continue with other tests ...


    
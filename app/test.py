from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Product, SOrder, SOItem
import traceback

class OrderProcessingTestCase(TestCase):
    def setUp(self):
        try:
            self.user = User.objects.create_user(username='testuser', password='password')
            self.product1 = Product.objects.create(
                type='Type 1',
                vcpus=2,
                memory=8,
                storage='100 GB SSD',
                network='1 Gbps',
                price=50.0
            )
            self.product2 = Product.objects.create(
                type='Type 2',
                vcpus=4,
                memory=16,
                storage='200 GB SSD',
                network='10 Gbps',
                price=100.0
            )
        except Exception as e:
            traceback.print_exc()
            raise e

    def tearDown(self):
        # Clean up after each test if needed
        pass

    def test_process_order_view(self):
        client = Client()
        client.force_login(self.user)

        try:
            response = client.post(reverse('process_order'), {
                'order_' + str(self.product1.id): '1',
                'quantity_' + str(self.product1.id): '2',
                'order_' + str(self.product2.id): '1',
                'quantity_' + str(self.product2.id): '1',
            })

            self.assertRedirects(response, reverse('checkout'))
            self.assertEqual(SOrder.objects.count(), 2)
            self.assertEqual(SOItem.objects.count(), 2)

        except Exception as e:
            traceback.print_exc()
            raise e

    def test_add_to_cart_view(self):
        client = Client()
        client.force_login(self.user)

        try:
            response = client.post(reverse('add_to_cart'), {
                'order_' + str(self.product1.id): '1',
                'quantity_' + str(self.product1.id): '2',
                'order_' + str(self.product2.id): '1',
                'quantity_' + str(self.product2.id): '1',
            })

            self.assertRedirects(response, reverse('instance_comparison'))
            self.assertEqual(self.user.cart_set.count(), 2)

        except Exception as e:
            traceback.print_exc()
            raise e

    def test_checkout_view(self):
        client = Client()
        client.force_login(self.user)

        try:
            response = client.get(reverse('checkout'))
            self.assertEqual(response.status_code, 200)

            SOrder.objects.create(
                AC=self.user.username,
                desc1=self.product1.description,
                SINTONO=1,
                DDATE=timezone.now().date(),
                NOTES=self.product1.notes,
            )
            SOItem.objects.create(
                PRODUCT=self.product1.type,
                UNITPRICE=self.product1.price,
                desc1=self.product1.description,
                VATRATE=2,
                SINTONO=1,
                QTY=2,
                NOTES='',
            )

            response = client.get(reverse('checkout'))
            self.assertContains(response, self.product1.type)
            self.assertContains(response, self.product1.price)
            self.assertContains(response, '2')

        except Exception as e:
            traceback.print_exc()
            raise e

    def test_instance_comparison_view(self):
        client = Client()
        client.force_login(self.user)

        try:
            response = client.get(reverse('instance_comparison'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, self.product1.type)
            self.assertContains(response, self.product2.type)

        except Exception as e:
            traceback.print_exc()
            raise e


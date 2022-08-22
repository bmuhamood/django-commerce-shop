from django.test import TestCase

from django.contrib.auth.models import User
from store.models import Product, Category

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug="django")

    def test_category_model_entry(self):
        """
        TestCategory model data Insertion/types/field attributes
        """

        data = self.data1
        self.assertTrue(isinstance(data, Category))
    
    def test_category_model_entry(self):
        """
        TestCategory model data Insertion/types/field attributes
        """

        data = self.data1
        self.assertEqual(str(data), 'django')

class TestProductsModel(TestCase):
      
      def setUp(self):
        #   Category.objects.create(name='django', slug="django")
        #   User.objects.create(username='bmuhamood')
          self.data1 = Product.objects.create(category=Category.objects.get(name='django'), user=User.objects.get(username='bmuhamood'), title='django', slug="django", description="django", price=10.00, image="django.jpg")
  
      def test_product_model_entry(self):
          """
          TestProduct model data Insertion/types/field attributes
          """
  
          data = self.data1
          self.assertTrue(isinstance(data, Product))
      
      def test_product_model_entry(self):
          """
          TestProduct model data Insertion/types/field attributes
          """
  
          data = self.data1
          self.assertEqual(str(data), 'django')
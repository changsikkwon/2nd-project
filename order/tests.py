import json
import re
import bcrypt
import jwt
import unittest

from django.test       import TestCase
from django.test       import Client
from unittest.mock     import patch, MagicMock

from user.models        import User
from product.models     import Product, Image
from .models            import Order, OrderItem

fake_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZGVudGlmaWVyIjoid2xkdXMxMjMifQ.oNOUNs-6XnGUw3gwgQC3M9EOPugekcyVUx2VNdLkJ2g'
fake_invalid_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZGVudGlmaWVyIjoid2xkdXMxMjMifQ.oNOUNs'

class CartTest(TestCase):
    def setUp(self):  
        User(
            id           = 1,
            name         = '김철수',
            identifier   = 'wldus123',
            password     = bcrypt.hashpw('1q2w3e4r!'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            birthdate    = '1994-08-01',
            gender       = '남자',
            phone_number = '01012345678'
        ).save()
        
        Product(
            id          = 1,
            korean_name = '화장품',
            price       = '4000000',
        ).save()
    
        Order(
            id   = 1,
            user = User.objects.get(id = 1),  
        ).save()
        
        OrderItem(
            id       = 1,
            order    = Order.objects.get(id = 1),
            product  = Product.objects.get(id = 1),
            quantity = 1,  
        ).save()
        
        Image(
            id        = 1,
            image_url = "https://www.abc.com.png",
            product   = Product.objects.get(id = 1),
        ).save()
             
    def tearDown(self):
        User.objects.all().delete()
        Product.objects.all().delete()
        Order.objects.all().delete()
        OrderItem.objects.all().delete()
        Image.objects.all().delete()
        
    def test_cart_post_success(self):
        client = Client(HTTP_Authorization = fake_token)
        
        data = {
            "product"  : 1,
            "quantity" : 1, 
            }
        
        response = client.post('/order/cart', json.dumps(data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message' : 'CART_ADDED'})
       
    def test_cart_post_key_error(self):
        client = Client(HTTP_Authorization = fake_token)
        
        data = {
            "item"     : 1,
            "quantity" : 1, 
            }
        
        response = client.post('/order/cart',json.dumps(data), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'KEY_ERROR'})
        
    def test_cart_post_invalid_login_error(self):
        client = Client()
        
        response = client.post('/order/cart',content_type = 'application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID_LOGIN'})

    def test_cart_post_invalid_token_error(self):
        client = Client(HTTP_Authorization = fake_invalid_token)
        
        response = client.post('/order/cart',content_type = 'application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID_TOKEN'})
               
    def test_cart_get_success(self):
        client = Client(HTTP_Authorization = fake_token)
        
        response = client.get('/order/cart', content_type = 'application/json')
        
        result = {
        "product_list": [
                {
                "order_id"   : 1,
                "product_id" : 1,
                "name"       : '화장품',
                "image_url"  : "https://www.abc.com.png",
                "price"      : 4000000,
                "quantity"   : 1
                }
            ]
        }
        
        self.assertEqual(response.json(), result)
        self.assertEqual(response.status_code, 200)
    
    def test_cart_get_invaild_login_error(self):
        client = Client()
        response = client.get('/order/cart', content_type = 'application/json')
        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID_LOGIN'})
        
    def test_cart_get_invaild_token_error(self):
        client = Client(HTTP_Authorization = fake_invalid_token)
        response = client.get('/order/cart', content_type = 'application/json')
        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID_TOKEN'})
    
    def test_cart_update_success(self):
        client = Client(HTTP_Authorization = fake_token)
        
        data = {
            'order_id'     : 1,
            'quantity'     : 3 
        }
        
        response = client.put('/order/cart', json.dumps(data), content_type = 'application/json')
        
        result = {
        "product_list":[
                {
                    "order_id"   : 1,
                    "product_id" : 1,
                    "name"       : '화장품',
                    "image_url"  : "https://www.abc.com.png",
                    "price"      : 4000000,
                    "quantity"   : 3
                }
            ]
        }
        
        self.assertEqual(response.json(), result)
        self.assertEqual(response.status_code, 200)   
        
    def test_cart_update_invalid_login_error(self):
        client = Client()
        response = client.put('/order/cart', content_type = 'application/json')
        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID_LOGIN'}) 
    
    def test_cart_update_invaild_token_error(self):
        client = Client(HTTP_Authorization = fake_invalid_token)
        response = client.put('/order/cart', content_type = 'application/json')
        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID_TOKEN'})
    
    def test_cart_delete_success(self):
        client = Client(HTTP_Authorization = fake_token)
        
        data = {
            'order_id' : 1,
        }
        
        response = client.delete('/order/cart', json.dumps(data), content_type = 'application/json')
        
        result = {
            "product_list":[]
        }
        
        self.assertEqual(response.json(), result)
        self.assertEqual(response.status_code, 200)  
        
    def test_cart_delete_invalid_login_error(self):
        client = Client()
        response = client.delete('/order/cart', content_type = 'application/json')
        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID_LOGIN'}) 
    
    def test_cart_delete_invaild_token_error(self):
        client = Client(HTTP_Authorization = fake_invalid_token)
        response = client.delete('/order/cart', content_type = 'application/json')
        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID_TOKEN'})
import json
import re
import bcrypt
import jwt
import unittest

from django.test       import TestCase
from django.test       import Client

from user.models        import User
from product.models     import Product
from .models            import Review

fake_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZGVudGlmaWVyIjoid2xkdXMxMjMifQ.oNOUNs-6XnGUw3gwgQC3M9EOPugekcyVUx2VNdLkJ2g'
fake_invalid_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZGVudGlmaWVyIjoid2xkdXMxMjMifQ.oNOUNs'

class ReviewTest(TestCase):
    def setUp(self):  
        user = User(
            id           = 1,
            name         = '김철수',
            identifier   = 'wldus123',
            password     = bcrypt.hashpw('1q2w3e4r!'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            birthdate    = '1994-08-01',
            gender       = '남자',
            phone_number = '01012345678'
        ).save()
        
        product = Product(
            id          = 1,
            korean_name = '화장품',
            price       = '4000000',
        ).save()
        
        Review(
            id           = 1,
            user_id      = 1,
            product_id   = 1,
            skin_type    = '지성',
            rating       = 5,
            comment      = '좋아요',
            review_image = 'http://www.abc.com.png',
        ).save()
             
    def tearDown(self):
        User.objects.all().delete()
        Product.objects.all().delete()
        Review.objects.all().delete()
        
    def test_review_post_success(self):
        client = Client(HTTP_Authorization = fake_token)
        
        data = {
            'comment'      : '좋아요',
            'rating'       : 5,
            'review_image' : 'http://www.abc.com.png',
            'product_id'   : 1,
            'skin_type'    : "건성"
            }
        
        response = client.post('/review', json.dumps(data), content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message' : 'REVIEW_SUCCESS'})
       
    def test_review_post_key_error(self):
        client = Client(HTTP_Authorization = fake_token)
        
        data = {
            'comment'      : '좋아요',
            'rating'       : 5,
            'image'        : 'http://www.abc.com.png',
            'product_id'   : 1,
            'skin_type'    : "건성"
            }
        
        response = client.post('/review',json.dumps(data), content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'KEY_ERROR'})
        
    def test_review_post_invalid_login_error(self):
        client = Client()
        
        response = client.post('/review',content_type = 'application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID_LOGIN'})

    def test_review_post_invalid_token_error(self):
        client = Client(HTTP_Authorization = fake_invalid_token)
        
        response = client.post('/review',content_type = 'application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID_TOKEN'})
    
    def test_review_delete_success(self):
        client = Client(HTTP_Authorization = fake_token)
        
        data = {
            'review_id' : 1,
        }
        
        response = client.delete('/review', json.dumps(data), content_type = 'application/json')
        
        result = {
            'message' : 'DELETE_SUCCESS'
        }
        
        self.assertEqual(response.json(), result)
        self.assertEqual(response.status_code, 200)  
        
    def test_review_delete_invalid_login_error(self):
        client = Client()
        response = client.delete('/review', content_type = 'application/json')
        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID_LOGIN'}) 
    
    def test_review_delete_invaild_token_error(self):
        client = Client(HTTP_Authorization = fake_invalid_token)
        response = client.delete('/review', content_type = 'application/json')
        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID_TOKEN'})
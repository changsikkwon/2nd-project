import jwt
import json
import unittest
import re
import bcrypt
import my_settings

from django.test            import Client, TestCase

from hyunlaneige.settings   import SECRET_KEY
from .models                import User
from unittest.mock          import patch, MagicMock

client = Client()

class SignupTest(TestCase):
    
    def setUp(self):  
        User(
            name         = '김철수',
            identifier   = 'cjftn123',
            birthdate    = '1995-03-27',
            password     = bcrypt.hashpw('1q2w3e4r!'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            gender       = '남자',
            phone_number = '01012345678',
        ).save()

    def tearDown(self):
        User.objects.all().delete()    
    
    def test_signup_exists_identifier(self):
        
        test_user = {
            'name'         : '김철수',
            'birthdate'    : '1995-03-27',
            'identifier'   : 'cjftn123',
            'password'     : '1q2w3e4r!',
            'gender'       : '남자',
            'phone_number' : '01012345258',
        }
        
        response = client.post('/user/signup', json.dumps(test_user), content_type = 'application/json')
        
        self.assertEqual(response.status_code, 400)   
        self.assertEqual(response.json(), {'message' : 'Already Used Identifier'})
        
    def test_signup_exists_phone_number(self):
        
        test_user = {
            'name'         : '김철수',
            'birthdate'    : '1995-03-27',
            'identifier'   : 'cjftn1234',
            'password'     : '1q2w3e4r!',
            'gender'       : '남자',
            'phone_number' : '01012345678',
        }
        
        response = client.post('/user/signup', json.dumps(test_user), content_type = 'application/json')
        
        self.assertEqual(response.status_code, 400)   
        self.assertEqual(response.json(), {'message' : 'Already Used Phone_number'})    
        
    def test_signup_validation_error_phone_number(self):
        
        test_user = {
            'name'         : '김철수',
            'birthdate'    : '1995-03-27',
            'identifier'   : 'cjftn1234',
            'password'     : '1q2w3e4r!',
            'gender'       : '남자',
            'phone_number' : '0101234',
        }
        
        response = client.post('/user/signup', json.dumps(test_user), content_type = 'application/json')
        
        self.assertEqual(response.status_code, 400)   
        self.assertEqual(response.json(), {'message' : 'Incorrect Phone_number Format'})
        
    def test_signup_validation_error_password(self):
        
        test_user = {
            'name'         : '김철수',
            'birthdate'    : '1995-03-27',
            'identifier'   : 'cjftn1234',
            'password'     : '1q2w',
            'gender'       : '남자',
            'phone_number' : '01012345671',
        }
        
        response = client.post('/user/signup', json.dumps(test_user), content_type = 'application/json')
        
        self.assertEqual(response.status_code, 400)   
        self.assertEqual(response.json(), {'message' : 'Incorrect Password Format'})
        
    def test_signup_key_error(self):
        
        test_user = {
            'name'         : '김철수',
            'birthdate'    : '1995-03-27',
            'identifier'   : 'cjftn123',
            'password'     : '1q2w3e4r!',
            'gender'       : '남자',
            'phone'        : '01012345678',
        }
        
        response = client.post('/user/signup', json.dumps(test_user), content_type = 'application/json')
        
        self.assertEqual(response.status_code, 400)   
        self.assertEqual(response.json(), {'message' : 'KEY_ERROR'})      
    
    def test_signup_success(self):
        
        test_user = {
            'name'         : '김영희',
            'birthdate'    : '1997-08-25',
            'identifier'   : 'dudgml123',
            'password'     : '1q2w3e4r!',
            'gender'       : '여자',
            'phone_number' : '01012325678',
        }
        
        response = client.post('/user/signup', json.dumps(test_user), content_type = 'application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message' : 'SUCCESS'})     
    
class SigninTest(TestCase):
    
    def setUp(self):
        User.objects.create(
            identifier = 'cjftn123',
            password   = bcrypt.hashpw('1q2w3e4r!'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            birthdate  = '1995-09-11',
        ).save

    def tearDown(self):
        User.objects.all().delete()

    def test_signin_success(self):
        
        test_user = {
            'identifier' : 'cjftn123',
            'password'   : '1q2w3e4r!'
        }
        
        token = jwt.encode({'identifier' : test_user['identifier']}, SECRET_KEY, algorithm = my_settings.algorithm)
        response = client.post('/user/signin', json.dumps(test_user), content_type = 'application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'token' : token.decode()}) 

    def test_signin_invalid_identifier(self):
        
        test_user = {
                'identifier' : 'dudgml123',
                'password'   : '1q2w3e4r!'
        }
        
        response = client.post('/user/signin', json.dumps(test_user), content_type = 'application/json')
        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {'message' : 'INVALID_USER'})

    def test_signin_invalid_password(self):
        
        test_user = {
                'identifier' : 'cjftn123',
                'password'   : '123456a!'
        }
        
        response = client.post('/user/signin', json.dumps(test_user), content_type = 'application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'INVALID_PASSWORD'})

    def test_signin_key_error(self):
        
        test_user = {
                'name'       : 'cjftn123',
                'password'   : '1q2w3e4r!'
        }
        
        response = client.post('/user/signin', json.dumps(test_user), content_type = 'application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message' : 'KEY_ERROR'})
        
class KakaoLoginTest(TestCase):
    def setUp(self):
        User(
            name         = '김철수',
            kakao_user   = '12345678'
        ).save()
        
    def tearDown(self):
        User.objects.all().delete()    
    
    @patch('user.views.requests')
    def test_kakao_signin_success(self, mocked_request):
        
        class FakeResponse:
            def json(self):
                return {
                    "id" : 12345678,
                    "properties"    : {"nickname": "김철수"},
                }
                
        mocked_request.get = MagicMock(return_value = FakeResponse())
        header             = {'HTTP_Authorization' : 'fake_token'}
        response           = client.get('/user/signin/kakao/callback', content_type = 'applications/json', **header)
        
        self.assertEqual(response.status_code, 200)
import json, requests, os, re
import traceback
import bcrypt
import jwt
import my_settings

from django.views               import View
from django.http                import JsonResponse, HttpResponse
from django.shortcuts           import redirect
from django.core.exceptions     import ObjectDoesNotExist

from hyunlaneige.settings       import SECRET_KEY, REST_API
from .validators                import password_validation_function, phone_number_validation_function
from .models                    import User

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if not(password_validation_function(data['password'])):
                return JsonResponse({'message' : 'Incorrect Password Format'}, status = 400)
            if not(phone_number_validation_function(data['phone_number'])):
                return JsonResponse({'message' : 'Incorrect Phone_number Format'}, status = 400)
            if User.objects.filter(identifier = data['identifier']).exists():
                return JsonResponse({'message' : 'Already Used Identifier'}, status = 400)
            if User.objects.filter(phone_number = data['phone_number']).exists():
                return JsonResponse({'message' : 'Already Used Phone_number'}, status = 400)
            
            signup_user = User(
                name         = data['name'],
                birthdate    = data['birthdate'],
                identifier   = data['identifier'],
                password     = data['password'],
                gender       = data['gender'],
                phone_number = data['phone_number'],
            )
            signup_user.full_clean()
            signup_user.password = bcrypt.hashpw(signup_user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            signup_user.save()
            
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

        return JsonResponse({'message' : 'SUCCESS'}, status = 200)

class SigninView(View):
    def post(self, request): 
        data = json.loads(request.body)
            
        try: 
            if User.objects.filter(identifier = data['identifier']).exists(): 
                signin_user    = User.objects.get(identifier = data['identifier'])
                input_password = data['password']
                
                if bcrypt.checkpw(input_password.encode('utf-8'), signin_user.password.encode('utf-8')): 
                    token = jwt.encode({'identifier' : signin_user.identifier}, SECRET_KEY, algorithm = my_settings.algorithm)
                    return JsonResponse({'token' : token.decode()}, status = 200)

                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status = 400)
            return JsonResponse({'message' : 'INVALID_USER'}, status = 401)
        except KeyError: 
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        
class KakaoSigninView(View):
    def get(self, request):
        client_id = REST_API
        redirect_uri = 'http://192.168.219.102:8000/user/signin/kakao/callback'
        return redirect(
            f'https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code'
        )
        
class KakaoSignInCallbackView(View):
    def get(self, request):

        try:
            code = request.GET.get('code')
            client_id = REST_API
            redirect_uri = 'http://192.168.219.102:8000/user/signin/kakao/callback'

            token_request = requests.get(
                f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}'
            ).json()

            access_token = token_request.get('access_token')

            profile_request = requests.get(
            'https://kapi.kakao.com/v2/user/me',
            headers = {"Authorization":f"Bearer {access_token}"}
            ).json()

            kakao_account    = profile_request.get('kakao_account')
            kakao_properties = profile_request.get('properties')
            kakao_id         = profile_request.get('id')
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

        except access_token.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_TOKEN'}, status = 400)
           
        if User.objects.filter(kakao_user = kakao_id).exists():
            user  = User.objects.get(kakao_user = kakao_id)
            token = jwt.encode({'kakao_user' : user.kakao_user}, SECRET_KEY, algorithm = my_settings.algorithm)
        
            return JsonResponse({'token' : token.decode()}, status = 200)

        else:
            User(
                kakao_user  = kakao_id,
                name        = kakao_properties['nickname'],
            ).save()
            
            user  = User.objects.get(kakao_user = kakao_id)
            token = jwt.encode({'kakao_user' : user.kakao_user}, SECRET_KEY, algorithm = my_settings.algorithm)
        
            return JsonResponse({'token' : token.decode()}, status = 200)
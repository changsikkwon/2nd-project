import jwt
import json
import requests
import my_settings

from functools              import wraps
from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from hyunlaneige.settings   import SECRET_KEY
from .models                import User

def login_required(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        if 'Authorization' not in request.headers:
            return JsonResponse({'message' : 'INVALID_LOGIN'}, status = 401)
        token = request.headers.get('Authorization')
        
        try:
            user_token   = jwt.decode(token, SECRET_KEY, algorithm = my_settings.algorithm)
            user         = User.objects.get(identifier = user_token['identifier'])
            request.user = user

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'INVALID_TOKEN'}, status = 401)

        except User.DoesNotExist:
            return JsonResponse({'message' : 'THIS ACCOUNT DOES NOT EXIST'}, status = 401)

        return func(self, request, *args, **kwargs)
    return wrapper
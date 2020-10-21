from django.core.validators   import RegexValidator

import re

def password_validation_function(value):
    regex_password = re.compile('^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$')
    return regex_password.search(value)

def phone_number_validation_function(value):
    regex_phone_number = re.compile('^\+?1?\d{9,15}$')
    return regex_phone_number.search(value)
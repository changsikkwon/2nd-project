from django.urls  import path, include

from .views       import ReviewView

urlpatterns = [
    path('', ReviewView.as_view()), 
]
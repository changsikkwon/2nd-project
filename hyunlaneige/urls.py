from django.urls import (
    path,
    include
)

urlpatterns = [
    path('user', include('user.urls')),
    path('product', include('product.urls')),
    path('order', include('order.urls')),
    path('review', include('review.urls')),
]
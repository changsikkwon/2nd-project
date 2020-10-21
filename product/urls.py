from django.urls import (
    path,
    include
)

from .views     import (
    ProductListView,
    ProductDetailView,
    ProductTypeListView,
    ProductSearchView
)
urlpatterns = [
    path('/list', ProductListView.as_view()), 
    path('/list/<int:product_id>', ProductDetailView.as_view()), 
    path('/type/list', ProductTypeListView.as_view()),
    path('/search',ProductSearchView.as_view())
]
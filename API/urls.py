from django.urls import path
from .views import AddCategoryEndpoint, CategoryListEndpoint, ProductsAddListEndpoint

urlpatterns = [
    path('categories', CategoryListEndpoint.as_view(), name="category"),
    path('add/categories', AddCategoryEndpoint.as_view(), name="add-cate"),
    path('products', ProductsAddListEndpoint.as_view(), name="products"),
]

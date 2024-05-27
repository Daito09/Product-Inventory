from django.urls import path
from .views import AddCategoryEndpoint, CategoryListEndpoint,ProductsEndpoint

urlpatterns = [
    path('add/categories', AddCategoryEndpoint.as_view(), name="add_cate"),
    path('categories', CategoryListEndpoint.as_view(), name="category"),
    path('products', ProducEndpoint.as_view(), name="products"),
]

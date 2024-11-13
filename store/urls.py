from .views import StoreDetailView,StoreListAPIView,SubcategoryListCreateAPIView,SubcategoryDetailView,ProductListCreateAPIView,ProductDetailView,RestaurantListCreateAPIView,RestaurantDetailView
from django.urls import path


urlpatterns = [
    path('store/<int:id>', StoreDetailView.as_view(), name='store-detail-api'),
    path('stores/', StoreListAPIView.as_view(), name='stores-list-api'),
    path('restaurants/', RestaurantListCreateAPIView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('subcategories/', SubcategoryListCreateAPIView.as_view(), name='subcategory-list'),
    path('subcategories/<int:id>/', SubcategoryDetailView.as_view(), name='subcategory-detail'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
]   

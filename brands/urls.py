from django.urls import path
from . import views

app_name = 'brands'


urlpatterns = [
    path('brand_listview/',views.BrandListView.as_view(),name='brand_listview'),
    path('brand_createview/',views.BrandCreateView.as_view(),name='brand_createview'),
    path('brand_detailview/<int:pk>/',views.BrandDetailView.as_view(),name='brand_detailview'),
    path('brand_updateview/<int:pk>/',views.BrandUpdateView.as_view(),name='brand_updateview'),
    path('brand_deleteview/<int:pk>/',views.BrandDeleteView.as_view(),name='brand_deleteview'),
]

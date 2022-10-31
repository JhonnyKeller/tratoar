from django.urls import path
from . import views


app_name = 'admin_view'

urlpatterns = [
    path('admin_budget_view/',views.AdminBudgetView,name='admin_budget_view'),
    path('admin_categorie_view/',views.AdminCategorieView,name='admin_categorie_view'),
    path('admin_brand_view/',views.AdminBrandView,name='admin_brand_view'),
    path('admin_product_view/',views.AdminProductsView,name='admin_product_view'),
]

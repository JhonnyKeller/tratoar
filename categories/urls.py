from django.urls import path
from . import views

app_name = 'categories'


urlpatterns = [
    path('sub_listview/',views.SubListView.as_view(),name='sub_listview'),
    path('sub_createview/',views.SubCreateView.as_view(),name='sub_createview'),
    path('sub_detailview/<int:pk>/',views.SubDetailView.as_view(),name='sub_detailview'),
    path('sub_updateview/<int:pk>/',views.SubUpdateView.as_view(),name='sub_updateview'),
    path('sub_deleteview/<int:pk>/',views.SubDeleteView.as_view(),name='sub_deleteview'),
    path('categories_listview/',views.CatListView.as_view(),name='categories_listview'),
    path('categories_createview/',views.CatCreateView.as_view(),name='categories_createview'),
    path('categories_detailview/<int:pk>/',views.CatDetailView.as_view(),name='categories_detailview'),
    path('categories_updateview/<int:pk>/',views.CatUpdateView.as_view(),name='categories_updateview'),
    path('categories_deleteview/<int:pk>/',views.CatDeleteView.as_view(),name='categories_deleteview'),
]
s

from django.urls import path
from . import views

app_name = 'air_conditioners'

urlpatterns = [
    path('ac_listview/',views.AcListView.as_view(),name='ac_listview'),
    path('ac_createview/',views.AcCreateView.as_view(),name='ac_createview'),
    path('ac_detailview/',views.AcDetailView,name='ac_detailview'),
    path('ac_updateview/<int:pk>/',views.AcUpdateView.as_view(),name='ac_updateview'),
    path('ac_deleteview/<int:pk>/',views.AcDeleteView.as_view(),name='ac_deleteview'),
    path('ac_search/',views.AcSearch,name='ac_search'),
]

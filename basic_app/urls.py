from django.urls import path
from . import views


app_name = 'basic_app'

urlpatterns = [
    path('budgets/',views.budgetCreateView,name='budgets'),
    path('contactsent/',views.contactSend,name='contactsent'),
    path("by/<username>/",views.UserBudgets.as_view(),name="budget_user"),
    path("user_budgets/",views.UserBudgetView,name="single_budget"),
    path("delete/<int:pk>/",views.DeleteBudget.as_view(),name="delete"),
]

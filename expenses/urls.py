from django.urls import path

from .views import add_expenses, index

urlpatterns = [
    path('', index, name="expenses"),
    path('add-expenses', add_expenses, name="add-expenses"),
]

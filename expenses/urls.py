from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('test/' , views.test , name='test'),
    path('' , views.expense_list , name='list'),
]

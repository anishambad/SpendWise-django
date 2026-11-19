from django.shortcuts import render 
from django.http import HttpResponse
from django.db.models import Sum

from .models import Expense

def test(request) :
    return HttpResponse("Test page")

def expense_list(request) :
    expenses = Expense.objects.select_related('category')
    total = expenses.aggregate(total=Sum('amount'))['total'] or 0
    
    context = {
        'expenses': expenses,
        'total' : total,
    }
    
    return render(request , 'expenses/expense_list.html' , context)



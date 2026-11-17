from django.db import models
from datetime import date 

class Category(models.Model) :
    name = models.CharField(max_length=50 , unique=True)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'
        
    def __str__(self) :
        return self.name
    

class Expense(models.Model) :
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10 , decimal_places=2)
    date = models.DateField(default=date.today)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,blank=True)
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_recurring = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date' , '-id']
        
    def __str__(self):
        return f"{self.title} ({self.amount})"

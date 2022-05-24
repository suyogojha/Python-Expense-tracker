from django.db import models
from django.contrib.auth.models import User
# Create your models here.

TYPE = (
    ('positive', 'positive'),
    ('negative', 'negative'),
)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.FloatField()
    expense = models.FloatField(default=0)
    balance = models.FloatField(null=True, blank=True)
    
    
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.FloatField(null=True, blank=True)
    expense_type = models.CharField(max_length=100, choices=TYPE)
    
    def __str__(self):
        return self.name
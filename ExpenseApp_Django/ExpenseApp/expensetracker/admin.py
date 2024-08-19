from django.contrib import admin
from .models import Expense, Sheet, Income, CreditCardPayment, Withdrawl

# Register your models here.
admin.site.register(Expense)
admin.site.register(Sheet)
admin.site.register(Income)
admin.site.register(CreditCardPayment)
admin.site.register(Withdrawl)

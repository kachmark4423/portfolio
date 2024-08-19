from django import forms
from .models import Expense, Income, CreditCardPayment, Withdrawl, Sheet

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["date","amount","description",
                  "payType","creditCard","category"]
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ["date","amount","cashOrBank","description"]
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

class CreditCardPaymentForm(forms.ModelForm):
    class Meta:
        model = CreditCardPayment
        fields = ["date", "creditCard", "amount", "payType"]
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

class WithdrawlForm(forms.ModelForm):
    class Meta:
        model = Withdrawl
        fields = ["date", "amount"]
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

class SheetForm(forms.ModelForm):
    class Meta:
        model = Sheet
        fields = ["type", "year", "month"]
        widgets = {
            "type":forms.widgets.TextInput(attrs={"readonly":"readonly"})
        }
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ExpenseForm, IncomeForm, SheetForm, CreditCardPaymentForm, WithdrawlForm
from .models import Sheet

# Create your views here.
def index(request):
    '''
    This function renders the home page of the application.


    Parameters
    -----------
    None

    Return
    ------
    None
    '''
    return render(request,"expensetracker/index.html")

def add_sheet(request, sheet_type):
    '''
    This function renders the form for adding a new Sheet object.


    Parameters
    -----------
    sheet_type: str
        the type for the data that the Sheet is being created for (e.g. 'expense')

    Return
    ------
    None
    '''
    if request.method != "POST":
        form = SheetForm(initial={"type":sheet_type})
    else:
        form = SheetForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("expensetracker:list_sheets", sheet_type=sheet_type)
    
    context = {"form":form, "sheet_type":sheet_type}
    return render(request, "expensetracker/add_sheet.html", context=context)


def list_sheets(request, sheet_type):
    '''
    This function renders the list of "sheets" available for the given sheet type.


    Parameters
    -----------
    sheet_type: str
        the type for the data that the Sheet is being created for (e.g. 'expense')

    Return
    ------
    None
    '''
    sheets = Sheet.objects.filter(type=sheet_type)
    context = {"sheets":sheets, "sheet_type":sheet_type}
    return render(request, "expensetracker/list_sheets.html", context=context)

def view_records(request, sheet_id):
    '''
    This function renders a table of recrods for the given sheet.


    Parameters
    -----------
    sheet_id: int
        the id for the sheet that you are attempting to view

    Return
    ------
    None
    '''
    sheet = Sheet.objects.get(id=sheet_id)
    sheet_type = sheet.type

    if sheet_type == "expense":
        records = sheet.expense_set.order_by('date')
        template = "expensetracker/view_expenses.html"
    elif sheet_type == "income":
        records = sheet.income_set.order_by('date')
        template = "expensetracker/view_income.html"
    elif sheet_type == "ccPayment":
        records = sheet.creditcardpayment_set.order_by('date')
        template = "expensetracker/view_ccPyaments.html"
    elif sheet_type == "withdrawl":
        records = sheet.withdrawl_set.order_by('date')
        template = "expensetracker/view_withdrawls.html"
    

    context = {"records":records, "sheet":sheet}
    return render(request, template, context=context)


def add_expense(request, sheet_id):
    '''
    This function renders the form for you to add a new expense record.


    Parameters
    -----------
    sheet_id: int
        the id for the sheet that you what to associate the record to.

    Return
    ------
    None
    '''
    sheet = Sheet.objects.get(id=sheet_id)
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ExpenseForm()
    else:
        form = ExpenseForm(data=request.POST)
        if form.is_valid():
            new_expense = form.save(commit=False)
            new_expense.typeMonthYear = sheet
            new_expense.save()
            return redirect("expensetracker:view_expenses", sheet_id=sheet_id)

    context = {"form":form, "sheet":sheet}
    return render(request, "expensetracker/add_expense.html", context=context)
    

def add_income(request, sheet_id):
    '''
    This function renders the form for you to add a new income record.


    Parameters
    -----------
    sheet_id: int
        the id for the sheet that you what to associate the record to.

    Return
    ------
    None
    '''
    sheet = Sheet.objects.get(id=sheet_id)
    if request.method != 'POST':
        form = IncomeForm()
    else:
        form = IncomeForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.typeMonthYear = sheet
            new_entry.save()
            return redirect("expensetracker:view_income", sheet_id=sheet_id)
    
    context = {"sheet":sheet, "form":form}
    return render(request, "expensetracker/add_income.html", context=context)

def add_cc_payment(request, sheet_id):
    '''
    This function renders the form for you to add a new credit card payment record.


    Parameters
    -----------
    sheet_id: int
        the id for the sheet that you what to associate the record to.

    Return
    ------
    None
    '''
    sheet = Sheet.objects.get(id=sheet_id)
    if request.method != "POST":
        form = CreditCardPaymentForm()
    else:
        form = CreditCardPaymentForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.typeMonthYear = sheet
            new_entry.save()
            return redirect("expensetracker:view_records", sheet_id = sheet_id)
    
    context = {"form":form, "sheet":sheet}
    return render(request, "expensetracker/add_cc_payment.html", context=context)

def add_withdrawl(request, sheet_id):
    '''
    This function renders the form for you to add a new withdrawl record.


    Parameters
    -----------
    sheet_id: int
        the id for the sheet that you what to associate the record to.

    Return
    ------
    None
    '''
    sheet = Sheet.objects.get(id=sheet_id)
    if request.method != "POST":
        form = WithdrawlForm()
    else:
        form = WithdrawlForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.typeMonthYear = sheet
            new_entry.save()
            return redirect("expensetracker:view_records", sheet_id = sheet_id)
    
    context = {"form":form, "sheet":sheet}
    return render(request, "expensetracker/add_withdrawl.html", context=context)

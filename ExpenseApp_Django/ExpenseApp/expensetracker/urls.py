from django.urls import path
from . import views

app_name = "expensetracker"
urlpatterns = [
    path("", views.index, name="index"),
    path("add_sheet/<str:sheet_type>", views.add_sheet, name="add_sheet"),
    path("list_sheets/<str:sheet_type>", views.list_sheets, name="list_sheets"),
    path("view_recrods/<int:sheet_id>", views.view_records, name="view_records"),
    path("add_expense/<int:sheet_id>", views.add_expense, name="add_expense"),
    path("add_cc_payemnt/<int:sheet_id>", views.add_cc_payment, name="add_cc_payment"),
    path("add_income/<int:sheet_id>", views.add_income, name="add_income"),
    path("add_withdrawl/<int:sheet_id>", views.add_withdrawl, name="add_withdrawl"),
]
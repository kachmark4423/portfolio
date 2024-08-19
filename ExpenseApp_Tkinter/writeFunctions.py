import datetime as dt
import os
import pandas as pd
from initiateBudgetFiles import generate_all_files


def write_to_file(formType:str, year:str, month:str, day:str, input:dict):
    '''
        This function determines the appropriate function to call for adding
        a new record form the data received.

        Parameters:
        -----------
        formType: str
            a string representing the form the data was entered from
        year: str
            a string of the year for the given record event
        month: str
            the month for the given record event
        day: str
            the day for the given record event
        input: dict
            a dictionary of input values from the form


        Return:
        -----------
        None
    '''

    if formType == "expenses":
        add_to_expense_sheet(year,
                             month,
                             day,
                             input["amount"],
                             input["description"],
                             input["payType"],
                             input["cc"],
                             input["category"])
    elif formType == "income":
        add_to_income_sheet(year,
                             month,
                             day,
                             input["amount"],
                             input["description"],
                             input["cashBank"])
    elif formType == "ccPayments":
        add_to_cc_payment_sheet(year,
                             month,
                             day,
                             input["cc"],
                             input["amount"],
                             input["payType"])
    elif formType == "withdrawls":
        add_to_withdrawl_sheet(year,
                             month,
                             day,
                             input["amount"])
    else:
        print("Form type not recognized")


def add_to_expense_sheet(year,
                        month,
                        day,
                         amount,
                         description,
                         payType,
                         cc,
                         category):
    
    '''
        This function adds the new record into the appropriate expense file.

        Parameters:
        -----------
        year: str
            a string of the year for the given record event.
        month: str
            the month for the given record event
        day: str
            the day for the given record event
        amount: double
            The dollar amount for the given transaction
        description: str
            a short description of the transacton event
        payType: str
            the method of payment used for the transaction
        cc: str
            the credit card that was used if applicable
        category: str
            the category that the transaction falls into


        Return:
        -----------
        None
    '''
    
    full_date = "-".join([year.get(), month.get(), day.get()])

 
    mon = dt.date.fromisoformat(full_date).strftime("%b")
    file = f"expenses{mon.title()}{year.get()}.csv"
  

    expense_file_path = os.path.dirname(__file__)+f"\\expenses\\{file}"

    expense_df = pd.read_csv(expense_file_path)
    transaction = max(expense_df["Transaction"], default=0) + 1

    entry = {"Transaction":transaction,
            "Date":full_date,
            "Amount":amount.get(),
            "Description":description.get(),
            "PayType":payType.get(),
            "CC":cc.get(),
            "Category":category.get()}


    new_record = pd.DataFrame(entry, index=[0]).set_index("Transaction")
    new_record.to_csv(expense_file_path, mode="a", header=False)


def add_to_income_sheet(year,
                         month,
                         day,
                         amount,
                         description,
                         cash_bank,):
    '''
        This function adds the new record into the appropriate income file.

        Parameters:
        -----------
        year: str
            a string of the year for the given record event.
        month: str
            the month for the given record event
        day: str
            the day for the given record event
        amount: double
            The dollar amount for the given transaction
        description: str
            a short description of the transacton event
        cash_bank: str
            whether payment was cash or bank deposite


        Return:
        -----------
        None
    '''
    
    full_date = "-".join([year.get(), month.get(), day.get()])

 
    mon = dt.date.fromisoformat(full_date).strftime("%b")
    file = f"Income{mon.title()}{year.get()}.csv"
  

    expense_file_path = os.path.dirname(__file__)+f"\\Income\\{file}"

    expense_df = pd.read_csv(expense_file_path)
    transaction = max(expense_df["Transaction"], default=0) + 1

    entry = {"Transaction":transaction,
            "Date":full_date,
            "Amount":amount.get(),
            "Cash/Bank;":cash_bank.get(),
            "Description":description.get()}


    new_record = pd.DataFrame(entry, index=[0]).set_index("Transaction")
    new_record.to_csv(expense_file_path, mode="a", header=False) 


def add_to_withdrawl_sheet(year,
                         month,
                         day,
                         amount,):
    '''
        This function adds the new record into the appropriate withdrawl file.

        Parameters:
        -----------
        year: str
            a string of the year for the given record event.
        month: str
            the month for the given record event
        day: str
            the day for the given record event
        amount: double
            The dollar amount for the given transaction



        Return:
        -----------
        None
    '''
    
    full_date = "-".join([year.get(), month.get(), day.get()])

 
    mon = dt.date.fromisoformat(full_date).strftime("%b")
    file = f"withdrawls{year.get()}.csv"
  

    expense_file_path = os.path.dirname(__file__)+f"\\withdrawls\\{file}"

    expense_df = pd.read_csv(expense_file_path)
    transaction = max(expense_df["Transaction"], default=0) + 1

    entry = {"Transaction":transaction,
            "Date":full_date,
            "Amount":amount.get()}


    new_record = pd.DataFrame(entry, index=[0]).set_index("Transaction")
    new_record.to_csv(expense_file_path, mode="a", header=False)  

def add_to_cc_payment_sheet(year,
                         month,
                         day,
                         cc,
                         amount,
                         pay_type):
    '''
        This function adds the new record into the appropriate credit card payment  file.

        Parameters:
        -----------
        year: str
            a string of the year for the given record event.
        month: str
            the month for the given record event
        day: str
            the day for the given record event
        cc: str
            the credit card that was paid
        amount: double
            The dollar amount for the given transaction
        payType: str
            the method of payment used for the transaction



        Return:
        -----------
        None
    '''
    
    full_date = "-".join([year.get(), month.get(), day.get()])

 
    mon = dt.date.fromisoformat(full_date).strftime("%b")
    file = f"CCpayments{mon.title()}{year.get()}.csv"
  

    expense_file_path = os.path.dirname(__file__)+f"\\CCPayments\\{file}"

    expense_df = pd.read_csv(expense_file_path)
    transaction = max(expense_df["Transaction"], default=0) + 1

    entry = {"Transaction":transaction,
            "Date":full_date,
            "CC":cc.get(),
            "Amount":amount.get(),
            "PayType":pay_type.get()}


    new_record = pd.DataFrame(entry, index=[0]).set_index("Transaction")
    new_record.to_csv(expense_file_path, mode="a", header=False)

 
    








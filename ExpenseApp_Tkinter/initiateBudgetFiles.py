import csv
import datetime as dt
import os
from validations import check_file_existance

base_path = file_path = os.path.dirname(__file__)

def createIncomeFile():
    '''
        This function generates a starter csv file for income data

        Parameters:
        -----------
        None


        Return:
        -----------
        None
        '''
    columns = ["Transaction","Date","Amount","Cash/Bank","Description"]
    filename = base_path + "\Income\Income" + dt.date.today().strftime('%b') + str(dt.date.today().year) + ".csv"

    if check_file_existance(filename):
        pass
    else:
    
        with open(filename, 'w') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(columns)


def createExpenseFile():
    '''
        This function generates a starter csv file for expense data

        Parameters:
        -----------
        None


        Return:
        -----------
        None
    '''
    columns = ["Transaction","Date","Amount","Description","PayType","CC","Category"]
    filename = base_path+"\expenses\expenses" + dt.date.today().strftime('%b') + str(dt.date.today().year) + ".csv"
    
    if check_file_existance(filename):
        pass
    else:
    
        with open(filename, 'w') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(columns)
       
def createCreditCardPaymentsFile():
    '''
        This function generates a starter csv file for credit card payment data

        Parameters:
        -----------
        None


        Return:
        -----------
        None
    '''
    columns = ["Transaction","Date","CC","Amount","PayType"]
    filename = base_path + "\CCPayments\CCpayments" + dt.date.today().strftime('%b') + str(dt.date.today().year) + ".csv"

    if check_file_existance(filename):
        pass
    else:

        with open(filename, 'w') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(columns)

def generate_all_files():
    '''
        This function is used to call each of the file generation functions

        Parameters:
        -----------
        None


        Return:
        -----------
        None
    '''
    createIncomeFile()
    createExpenseFile()
    createCreditCardPaymentsFile() 


if __name__ == "__main__":
    createIncomeFile()
    createExpenseFile()
    createCreditCardPaymentsFile() 
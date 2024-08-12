import csv
import datetime as dt
import os
from validations import check_file_existance

base_path = file_path = os.path.dirname(__file__)#+f"\\expenses\\{file}"

def createIncomeFile():
    columns = ["Transaction","Date","Amount","Cash/Bank","Description"]
    filename = base_path + "\Income\Income" + dt.date.today().strftime('%b') + str(dt.date.today().year) + ".csv"

    if check_file_existance(filename):
        pass
    else:
    
        with open(filename, 'w') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(columns)


def createExpenseFile():
    columns = ["Transaction","Date","Amount","Description","PayType","CC","Category"]
    filename = base_path+"\expenses\expenses" + dt.date.today().strftime('%b') + str(dt.date.today().year) + ".csv"
    
    if check_file_existance(filename):
        pass
    else:
    
        with open(filename, 'w') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(columns)
       
def createCreditCardPaymentsFile():
    columns = ["Transaction","Date","CC","Amount","PayType"]
    filename = base_path + "\CCPayments\CCpayments" + dt.date.today().strftime('%b') + str(dt.date.today().year) + ".csv"

    if check_file_existance(filename):
        pass
    else:

        with open(filename, 'w') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(columns)

def generate_all_files():
    createIncomeFile()
    createExpenseFile()
    createCreditCardPaymentsFile() 


if __name__ == "__main__":
    createIncomeFile()
    createExpenseFile()
    createCreditCardPaymentsFile() 
from django.db import models
import datetime
import calendar

# Create your models here.
class Sheet(models.Model):
    '''
    This model is used to associate other models to a given transaction type, year, and month
    '''
    current_year = int(datetime.date.today().year)
    years = {year:year for year in range(2022, current_year+1)}
    months = {calendar.month_name[i]:calendar.month_name[i] for i in range(1, 13)}
    types = {"expense":"Expense", "ccPayment":"Credit Card Payment",
             "withdrawl":"Withdrawl", "income":"Income"}

    type = models.CharField(max_length=50, choices=types)
    year = models.SmallIntegerField(choices=years)
    month = models.CharField(max_length=20,choices=months)
    typeMonthYear = models.CharField(max_length=50, blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        self.typeMonthYear = self.type + str(self.month)+str(self.year)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.typeMonthYear

class Expense(models.Model):
    '''
    This model is used to store expense transactions
    '''
    payTypes = {"cash":"Cash", "cc":"Credit Card", "bank":"Bank"}

    ccList = {"visa":"Visa",
              "americanExpress":"American Express"}


    categories = {"groceries":"Groceries/Home Goods", "internet":"Internet Bill",
                "gasBill":"Gas Bill", "electricBill":"Electric Bill", "waterBill":"Water Bill",
                "disney":"Disney/Hulu", "gasoline":"Gasoline/Maintenance", "hobbies":"Hobbies",
                "outsideFood":"Outside Food", "homeRepairs":"Home Repairs", "mortgage":"Mortgage","other":"Other"}


    date = models.DateField()
    amount = models.DecimalField(max_digits=100,decimal_places=2)
    description = models.CharField(max_length=50)
    payType = models.CharField(max_length=50, choices=payTypes)
    creditCard = models.CharField(max_length=50,choices=ccList)
    category = models.CharField(max_length=50,choices=categories)
    typeMonthYear = models.ForeignKey(Sheet, on_delete=models.CASCADE, null=True)
    

class Income(models.Model):
    '''
    This model is used to store income transactions
    '''

    date = models.DateField()
    amount = models.DecimalField(max_digits=100,decimal_places=2)
    cashOrBank = models.CharField(max_length=50,choices={"cash":"Cash","bank":"Bank"})
    description = models.CharField(max_length=50)
    typeMonthYear = models.ForeignKey(Sheet, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'income'

class CreditCardPayment(models.Model):
    '''
    This model is used to store credit card payment transactions
    '''
    ccList = {"visa":"Visa",
              "americanExpress":"American Express"}
    
    payTypes = {"cash":"Cash", "bank":"Bank"}

    date = models.DateField()
    creditCard = models.CharField(max_length=50,choices=ccList)
    amount = models.DecimalField(max_digits=100,decimal_places=2)
    payType = models.CharField(max_length=50, choices=payTypes)
    typeMonthYear = models.ForeignKey(Sheet, on_delete=models.CASCADE, null=True)

class Withdrawl(models.Model):
    '''
    This model is used to store withdrawl transactions
    '''
    date = models.DateField()
    amount = models.DecimalField(max_digits=100,decimal_places=2)
    typeMonthYear = models.ForeignKey(Sheet, on_delete=models.CASCADE, null=True)

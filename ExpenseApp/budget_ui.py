import tkinter as tk
from tkinter import ttk
from writeFunctions import write_to_file
from initiateBudgetFiles import generate_all_files


class ExpenseTracker(tk.Tk):
    def __init__(self):

        super().__init__()
        self.title("Budget Tracker")
        self.geometry('1200x600')
        self.minsize(600,600)
      
        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")


        self.mainPage = MainPage(container, self)
        self.expenseForm = EntryForm(container, self, formType="expenses",
                                     inputs=[{"label":"Amount", "widget":"entry", "textVariable":"amount"},
                                            {"label":"Description", "widget":"entry", "textVariable":"description"},
                                            {"label":"PayType", "widget":"combobox", "textVariable":"payType", "values":["Cash", "Bank", "CC"]},
                                            {"label":"CC", "widget":"combobox", "textVariable":"cc", "values":["", "Visa", "American Express"]},
                                            {"label":"Category", "widget":"combobox", "textVariable":"category", "values":["Groceries/Home Goods", "Internet Bill",
                                                                                                                        "Gas Bill", "Electric Bill", "Water Bill",
                                                                                                                        "Disney/Hulu", "Gasoline/Maintenance", "Hobbies",
                                                                                                                        "Outside Food", "Home Repairs", "Mortgage","Other"]}], 
                                            amount=tk.DoubleVar(), description=tk.StringVar(), payType=tk.StringVar(), cc=tk.StringVar(), category=tk.StringVar())
        self.incomeForm = EntryForm(container, self, formType="income",
                                     inputs=[{"label":"Amount", "widget":"entry", "textVariable":"amount"},
                                             {"label":"Cash/Bank", "widget":"combobox", "textVariable":"cashBank", "values":["Cash", "Bank"]},
                                             {"label":"Description", "widget":"entry", "textVariable":"description"}], 
                                            amount=tk.DoubleVar(), description=tk.StringVar(), cashBank=tk.StringVar())
        self.ccPaymentForm = EntryForm(container, self, formType="ccPayments",
                                     inputs=[{"label":"CC", "widget":"combobox", "textVariable":"cc", "values":["Visa", "American Express"]},
                                             {"label":"Amount", "widget":"entry", "textVariable":"amount"},
                                             {"label":"PayType", "widget":"combobox", "textVariable":"payType", "values":["Cash", "Bank"]},
                                            ], 
                                            amount=tk.DoubleVar(), payType=tk.StringVar(), cc=tk.StringVar())
        self.withdrawlForm = EntryForm(container, self, formType="withdrawls",
                                     inputs=[{"label":"Amount", "widget":"entry", "textVariable":"amount"}], 
                                            amount=tk.DoubleVar())

        self.mainPage.grid(row=0, column=0, sticky="nsew")
        self.expenseForm.grid(row=0, column=0, sticky="nsew")
        self.incomeForm.grid(row=0, column=0, sticky="nsew")
        self.ccPaymentForm.grid(row=0, column=0, sticky="nsew")
        self.withdrawlForm.grid(row=0, column=0, sticky="nsew")

        #self.current_page = self.mainPage

    
        self.display_page(self.mainPage)



    def display_page(self, pageToBeDisplayed):
        if hasattr(pageToBeDisplayed, "clearForm"):
            pageToBeDisplayed.clearForm()
        pageToBeDisplayed.tkraise()
        

class EntryForm(ttk.Frame):

    def __init__(self, container, master, formType, inputs, **variables):

        super().__init__(container)

        year_list = [str(x) for x in range(2022, 2030)]
        month_list = [f"{x:02d}" for x in range(1, 13)]
        day_list = [f"{x:02d}" for x in range(1, 32)]

        year = tk.StringVar()
        month = tk.StringVar()
        day = tk.StringVar()
        
        self.comboboxes = []
        self.entries = []

        ttk.Label(self, text="Year").grid(column=0, row=0)
        year_widget = ttk.Combobox(self, values=year_list, state="readonly", textvariable=year)
        year_widget.grid(column=0, row=1)
        
        ttk.Label(self, text="Month").grid(column=1, row=0)
        month_widget = ttk.Combobox(self, values=month_list, state="readonly", textvariable=month)
        month_widget.grid(column=1, row=1)

        ttk.Label(self, text="Day").grid(column=2, row=0)
        day_widget = ttk.Combobox(self, values=day_list, state="readonly", textvariable=day)
        day_widget.grid(column=2, row=1)

        self.comboboxes += [year_widget, month_widget, day_widget]

        for i, input in enumerate(inputs):
            ttk.Label(self, text=input["label"]).grid(column=3+i, row=0)
            var = variables[input["textVariable"]]
            if input["widget"] == "entry":
                widget = ttk.Entry(self, textvariable=var)
                widget.grid(column=3+i, row=1)
                self.entries.append(widget)
            if input["widget"] == "combobox":
                widget = ttk.Combobox(self,values=input["values"], textvariable=var, state='readonly')
                widget.grid(column=3+i, row=1)
                self.comboboxes.append(widget)
            

        ttk.Button(self, text="Submit Entry", command=lambda: write_to_file(formType, year, month, day, variables)).grid(column=0, row=2)
        ttk.Button(self, text="Clear All", command=lambda: self.clearForm()).grid(column=1, row=2)
        ttk.Button(self, text="Main", command=lambda: master.display_page(master.mainPage) ).grid(column=2, row=2)

    def clearForm(self):
        for cb in self.comboboxes:
            cb.set("")
        for e in self.entries:
            e.delete(0,tk.END)
       
      

class MainPage(ttk.Frame):
    def __init__(self, container, master):
        super().__init__(container)
        self.master = master
   
        ttk.Button(self, text="Add Expense", command=lambda: master.display_page(master.expenseForm), width=16).grid(column=0, row=0)
        ttk.Button(self, text="Add Income", command=lambda: master.display_page(master.incomeForm), width=16).grid(column=0, row=1)
        ttk.Button(self, text="Add CC Payment", command=lambda: master.display_page(master.ccPaymentForm), width=16).grid(column=0, row=2)
        ttk.Button(self, text="Add Withdrawl", command=lambda: master.display_page(master.withdrawlForm),  width=16).grid(column=0, row=3)
        ttk.Button(self, text="Add New Files", command=generate_all_files,  width=16).grid(column=0, row=4)

if __name__ == "__main__":        
    app = ExpenseTracker()
    app.mainloop()
from bill import *
from flatmate import *
from pdf_report import *

bill = Bill(name="Electricity", amount=120, period= "March 2021")
john = Flatmate("John", 20)
mary = Flatmate("Mary", 25)
print(f"John pays: £{john.pays(bill=bill, flatmate2=mary)}")
print(f"Mary pays: £{mary.pays(bill=bill, flatmate2=john)}")
from bill import *
from flatmate import *
from pdf_report import *

name = input("Enter the type of bill? ")
amount = float(input("Enter the bill amount? "))
period = input("What month of the year is the bill for? ")

bill = Bill(name, amount, period)
john = Flatmate("John", 20)
mary = Flatmate("Mary", 25)
print(f"John pays: £{round(john.pays(bill=bill, flatmate2=mary), 2)}")
print(f"Mary pays: £{round(mary.pays(bill=bill, flatmate2=john), 2)}")

pdf_report = PDFReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=mary, bill=bill)
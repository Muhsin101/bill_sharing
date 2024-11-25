from bill import *
from flatmate import *
from pdf_report import *

bill_name = input("Enter the type of bill? ")
amount = float(input("Enter the bill amount? "))
period = input("What month of the year is the bill for? ")
bill = Bill(bill_name, amount, period)

name1 = input("What is your name? ")
days_in_house1 = float(input(f"How many days did you: {name1} stay in house? "))
flatmate1 = Flatmate(name1, days_in_house1)

name2 = input("What is your flatmates name? ")
days_in_house2 = float(input("How many days did your flatmate stay in house? "))
flatmate2 = Flatmate(name2, days_in_house2)
print(f"{name1} pays: £{round(flatmate1.pays(bill, flatmate2), 2)}")
print(f"{name2} pays: £{round(flatmate2.pays(bill, flatmate1), 2)}")

pdf_report = PDFReport(filename=f"{bill_name}{bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill)
from django.db import models

# Create your models here.



# Create Invoice class so you can instantiate a new invoice and not have to worry with things like "invoice[3]" to pull values
class Invoice:
  def __init__(self, invoice_number, customer_name, date, lead, amount, agreements_sold, service_type, callback, callback_date, callback_notes, no_money):
    self.invoice_number=int(invoice_number) #converts invoice_number data to integer, because it's imported as a string
    self.customer_name=customer_name
    self.amount=float(amount) # amount is floated because it's a decimal, otherwise you end up with a lot of rounded numbers.
    self.date=date
    self.lead=lead
    self.agreements_sold=int(agreements_sold)
    self.service_type=service_type
    self.callback=callback
    self.callback_date=callback_date
    self.callback_notes=callback_notes
    self.no_money=no_money

# Create Employee class so you can instantiate employee time records without worryiing about things like "employee[5]" to pull values
class Employee:
  def __init__(self, employee_name, invoice_number): #, hours_sold, hours_billed, date):
    self.employee_name=employee_name
    self.invoice_number=int(invoice_number)
#    self.hours_sold=float(hours_sold)
#    self.hours_billed=float(hours_billed)
#    self.date=date


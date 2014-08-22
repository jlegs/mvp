




import sys
import datetime
import calendar
import gspread
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plot
import numpy

current=datetime.datetime.now()
date=str(current.month)+"-"+str(current.day)+"-"+str(current.year)

gc = gspread.login(sys.argv[1], sys.argv[2])
invoice_spreadsheet=gc.open("Invoices (Responses)")
time_spreadsheet=gc.open("Time Cards (Responses)")

timesheet=time_spreadsheet.worksheet("Form Responses")
invoice_sheet=invoice_spreadsheet.worksheet("Form Responses")
# The following two arrays set the initial data sets
employee_time = timesheet.get_all_values()
invoice_row_data = invoice_sheet.get_all_values()
#print employee_time
#print invoice_row_data

#delete first entry in "invoice_list" and "employee_time" because it's just header information
del invoice_row_data[0]
del employee_time[0]
#print invoice_row_data[0]
#print employee_time[0]
global_employee_time_cards=[]
global_invoice_array=[]

# temp_time_row_data array is used to filter out None values that for some reason appeared in the data.
# After the filter is done, it sets the good values into time_row_data
temp_time_row_data=[]
time_row_data=[]
temp_invoice_data=[]
invoice_data=[]


# This iterates through to add *all* rows in the time sheet spreadsheet to a temporary array
# It's temporary so that we can remove "None" values, which are showing up for some reason
for i in employee_time:
  if i[0]!="" and i[1]!="":
    temp_time_row_data.append(i)

# This adds only rows that are not filled with "None" data to the time_row_data list.
for x in temp_time_row_data:
  if x[0] != None and x[1] != None and x[0]!="" and x[1]!="":
   time_row_data.append(x)


for item in invoice_row_data:
  if item[0] != None and item[1] != None and item[0]!="" and item[1]!="":
    temp_invoice_data.append(item)


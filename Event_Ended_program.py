import openpyxl

# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))

# # Calculate the ending time
# hour1 = hour + (mins + dura) // 60
# hour_new = hour1 + hour
# end_hour =(dura//60)
# mins = (mins + dura) % 60
# end_mins= dura
# # hour = hour % 24

# print("Ending time is :", hour, ":", mins)
# print("Duration of Hours is :",end_hour, "and the duration of minutes is:",end_mins)

# print("The event ended at", hour, ":", mins, )

# Create a new Excel workbook
workbook = openpyxl.Workbook()
sheet = workbook.active

# Write data to the Excel file
# Replace the placeholders with the actual values
# sheet['A1'] = hour
# sheet['B1'] = mins
# sheet['C1'] = end_hour
# sheet['D1'] = end_mins

# Save the workbook
workbook.save('/a:/python_practice/python/Day06/Event_Data.xlsx')


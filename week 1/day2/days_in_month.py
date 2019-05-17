"""
Hands On 3
"""
# Make a function days_in_month to return the number of days in a specific month of a year




year = input("enter year")
month =raw_input("enter month")

def days_in_month(month,year):
    if(year % 4 == 0 and (month == 'sept' or month == 'april' or month == 'june' or month == 'nov' or month == 'feb')):
        if(month == 'feb'):
            return 29
        else:
            return 30
    elif (month == 'jan' or month == 'march' or month == 'may' or month == 'july' or month == 'feb' or month == 'march' or month == 'august' or month == 'oct' or month == 'dec'):
        if(month == 'feb'):
            return 28
        else:
            return 31
     
print(days_in_month(month,year))        
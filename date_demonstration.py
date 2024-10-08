# Using python built in

# Import the datetime library to use it in the program
import datetime

# Assign the current date and time to a variable
time = datetime.datetime.now()
month = time.month
month_word = time.strftime("%B")

# Display date/time
print(f"The current date and time is {time}")
print(f"The current month is {month}")
print(f"The current month is{month_word}")

today = datetime.datetime.today()
print(f"Today is {today}")

weekday = today.weekday()
weekday = int(weekday)
print(f"The day of the week is {weekday}/n")

# Gets the datatype of the variables
print(type(weekday))
print()
'''
# Get day of week from user as integer
weekday = int(input("Enter an integer 0-6 as the day of the week"))
'''
# if-else statement to determine day of the week

if weekday == 0:
      weekday_word = "monday"


elif weekday == 1:
      weekday_word = "tuesday"


elif weekday == 2:
      weekday_word = "wednesday"


elif weekday == 3:
      weekday_word = "thursday"


elif weekday == 4:
      weekday_word = "friday"


elif weekday == 5:
      weekday_word = "saturday"


elif weekday == 6:
      weekday_word = "sunday"

else:
    print("Invalid day of the week!!!")
    weekday_word = "INVALID"

print()
print(f"The day of the week is {weekday_word}")






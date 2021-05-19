import datetime

person = input("What is your full name?")
print("Hello", person, "!")

# Asking the user to input their date of birth
# .strftime converts a 'datetime' object consisting of current date and time into different string types
# .date was used to produce the year, month and days only
birthDate = input("Enter your birth date (dd/mm/yyyy)\n----> ")
birthDate = datetime.datetime.strptime(birthDate, "%d/%m/%Y").date()
print("Your birthday is on "+ birthDate.strftime("%d") + " of " + birthDate.strftime("%B, %Y"))

# This produces todays date
currentDate = datetime.datetime.today().date()

# Calculating the age
age = currentDate.year - birthDate.year
monthDate = currentDate.month - birthDate.month
dateDate = currentDate.day - birthDate.day

# Converting the type
age = int(age)
monthDate = int(monthDate)
dateDate = int(dateDate)

# This helps calculates the error that produces the wrong age for example someone who was born on the 13/06/2000 is 20 until 12/06/2021
if monthDate < 0:
    age = age-1
elif dateDate < 0 and monthDate == 0:
    age = age-1

#lets print the age now
print("Oh my God! you are {0:d}".format(age), "years old!")


# Converting date of birth into hours
# 365 days * 24 hours
hours = 8760 * age
# 365 days * 1440 minutes in a day
minutes = 525600 * age
# 365 days * 86400 seconds in a day
seconds = 31536000 * age




from datetime import date

# Get user's date of birth
year = int(input("Enter your birth year (YYYY): "))
month = int(input("Enter your birth month (1-12): "))
day = int(input("Enter your birth day (1-31): "))

# Create a date object for the date of birth
dob = date(year, month, day)

# Get today's date
today = date.today()

# Calculate the age
age = today.year - dob.year

# Adjust for cases where the birth date hasn't occurred yet this year
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

# Display the result
print(f"You are {age} years old.")

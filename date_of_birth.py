from datetime import date, timedelta

# Get today's date
today = date.today()

# Get user's age, birth month, and birth day as input
age = int(input("Enter your age: "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

# Calculate approximate year of birth
year_of_birth = today.year - age

# Create the birth date
birth_date = date(year_of_birth, birth_month, birth_day)

# If the birth date is in the future, subtract one year
if birth_date > today:
    birth_date = birth_date.replace(year=year_of_birth - 1)

# Display the result
print(f"Your date of birth is: {birth_date.strftime('%d-%m-%Y')}")




date_of_birth = input("Enter your date of birth (yyyy-mm-dd): ")
age = 2025 - int(date_of_birth[:4])
print(f"You are {age} years old.")

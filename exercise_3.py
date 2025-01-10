# Description: This program is to calculate the total and average salary of an
# employee for a year.
my_annual_salary = [
    45056, 45126, 45985, 45852, 45425, 45698,
    45236, 45896, 45285, 45785, 45698, 45896
]
# returns the sum of all the elements in the list of my_annual_salary.
total_salary = sum(my_annual_salary)
average_salary = total_salary / 12  # returns the average of the total salary.
print(f"My total salary is Rs. {total_salary}")
print(f"My average salary is Rs. {average_salary}")


# Exercise 4
list_salary = []
n_salary = int(input("Enter the number of months you got the salary: "))
for i in range(0, n_salary):
    salary = int(input())
    list_salary.append(salary)
print(list_salary)
sum = 0
i = 0
while i < len(list_salary):
    sum = sum + list_salary[i]
    i = i + 1
average = sum/n_salary
print(f"Total salary is Rs. {sum}")
print(f"Average salary is Rs. {average}")

# Description: This program is to calculate the total and average salary of an
# employee for a year.
my_annual_salary = [
    45056, 45126, 45985, 45852, 45425, 45698,
    45236, 45896, 45285, 45785, 45698, 45896
]
# returns the sum of all the elements in the list of my_annual_salary.
total_salary = sum(my_annual_salary)
average_salary = total_salary / 12  # returns the average of the total salary.
print(f"My total salary is Rs. {total_salary}")
print(f"My average salary is Rs. {average_salary}")

# Exercise 4
list_salary = []
n_salary = int(input("Enter the number of months you got the salary:  "))
for i in range(0, n_salary):
    salary = int(input())
    list_salary.append(salary)


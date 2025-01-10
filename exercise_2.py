
english = int(input("english "))
math =  int(input("math"))
science = int(input("science"))
nepali = int(input("nepali"))
social = int(input("social"))

total = (english + math + science + nepali + social)
percentage = (total / 500) * 100
average = total / 5
print(f"Total marks: {total}")
print(f"Percentage: {percentage}")
print(f"Average: {average}")
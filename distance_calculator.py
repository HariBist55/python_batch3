principle = 50000
rate = 1.2
time = 5
interest = (principle * rate * time)/100
print(f"Simple Interest is Rs. {interest}")
print(f"Total amount is Rs. {principle + interest}")
print(f"Total amount is Rs. {principle + (principle * rate * time)}")

dis_from_home_to_office = 15 #km
speed = 40 #km/h
min = 60 #60/hour
time = (dis_from_home_to_office / speed)*(min)
print(f"Time taken to reach office is {time} mins")
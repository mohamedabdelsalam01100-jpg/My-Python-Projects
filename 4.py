import datetime
names = ["Ahmed", "Sara", "Ali"]
ages = [20, 15, 25]


list1 = zip(names, ages)
hours = lambda age: age *365*24

final = filter(lambda x : x[1]>= 18, list1)
with open("data.txt","w") as file:
    for name,age in final:
      file.write(f"{name} - Age: {age} - Hours: {hours(age)} - Date: {datetime.date.today()}\n")
file = open("data.txt", "r")
print(file.read())
file.close()



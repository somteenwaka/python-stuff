from ast import Num


age = 20

if age < 18:
    print("still growing")
elif age > 18 and age < 21:
    print("you're an adolescent")
else:
    print("you're an adult")

users = ["Somto, Adaobi, Chike, Nwaka"]
for user in users:
    print(user)

num = 10
stepper = 0
while (stepper < 10):
    print(stepper)
    stepper += 1

# while (stepper < Num):
#     if (stepper % 2) == 0:
#      print(stepper)
   

index = 0
lenght = len (users)
while index < lenght:
    print(users[index])
    index +=1

nums = range(51)
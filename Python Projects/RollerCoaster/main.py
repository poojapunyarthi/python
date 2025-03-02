print("Welcome to the RollerCoaster!!!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster..")
  age = int(input("What is your age? "))
  
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
    
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
    
# logical operator used (and)
  elif age >= 45 and age <= 55:
    print("Have a free ride on us!")
  
  else:
    bill = 12
    print("Adult tickets are $12.")
    
  photo = input("Do you want a photo? Y or N: ")
  if photo == "Y":
    print("You have to pay $3 extra.")
    bill += 3
    print(f"Your total bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride")

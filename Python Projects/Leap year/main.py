print("Leap year or not leap year")
year = int(input("Enter a year: "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("leap year")
    else:  
     print("Not a Leap year")
  else:
    print("leap year")
else:
 print("Not leap year")
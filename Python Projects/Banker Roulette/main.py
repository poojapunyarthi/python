names = ["Pooja" , "Akshay", "Mohit" , "Shweta", "Sneha", "Dhaval"]

import random

number_items = len(names)

random_choice = random.randint(0,number_items -1)

person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")
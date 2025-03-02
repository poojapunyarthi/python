print("Life Calculator")
age = input("Enter age:")
age_int = int(age)
years = 90 - int(age)
weeks = years * 52
days = years * 365
print(f"You have {years} years, {weeks} weeks, {days} days left.")
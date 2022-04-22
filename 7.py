CURRENT_YEAR = 2022
		
print("Your fristname: ")
firstname = input()

print("Your lastname: ")
lastname = input()

print("Your name is " + firstname + " " + lastname )

print("When you were born: ")
year_born = input()
year_born = int(year_born)

age = CURRENT_YEAR - year_born

print("Your are " + str(age) + " yaer old in " + str(CURRENT_YEAR))
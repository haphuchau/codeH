CURRENT_YEAR = 2022
METER_TO_FEET = 3.281	

firstname = input("Your fristname: ")
lastname = input("Your lastname: ")
year_born = int(input("When you were born: "))
height_meter = float(input("Your height (meter): "))

age = CURRENT_YEAR - year_born

height_feet = height_meter * METER_TO_FEET
height_feet = round(height_feet,1)

print("\n-----")
print( "Your are " + str(height_feet) + " feet tall " )
print("{2} is {0} year old in {1}".format(age,CURRENT_YEAR,firstname))
print("Your name is: {0} {1} ".format(firstname,lastname))

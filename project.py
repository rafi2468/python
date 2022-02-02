""" name = ["rafi""ashfaq""hussain"]
for i in range(0,6):
    try :
        print(names[i])
    except:
        print("There is no more name")

print("program continuing") """


""" age = ""
while isinstance(age,str):
    try:
        age = int(input("Enter age:"))
    except:
        print("error")

print("success") """

""" 
temp = 0
totaltemp = 0
numberoftemps = 0
print("enter next temp")
temp =int(input(""))
while temp != -100:
    totaltemp += temp
    numberoftemps += 1
    print("enter next temp")
    temp =int(input(""))
averagetemp = totaltemp/numberoftemps
print(averagetemp) """
                

print("enter w for weekend , b for bank holiday or d for weekday")
day = input("")
print("enter a for adult , c for child")
visitor = input("")
if ((day == "w") or (day == "b")) and (visitor == "a"):
    charge = 12.0
elif ((day == "w") or (day == "b")) and (visitor == "c"):
    charge = 7.5
elif (visitor == "a"):
    charge = 8.0
else:
    charge = 5.0
print(charge)
     




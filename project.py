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
print(averagetemp)
                




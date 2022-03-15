mylist = ["bob","ana","jim", "jak","tim"] 
found = False
searched = "henry"
i = 0
while found == False and i<len(mylist):
    if mylist[i]== searched:
         print ("found at" , i)
         found = True
    i  = i+1
print("done")
if found == False:
    print("Item not found")    
print("done")    
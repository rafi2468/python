mylist = ["bob","ana","jim", "jak","tim"] 
mylist.sort()
found = False
start = 0
end = len(mylist)-1
s = "jhon"
while found == False and start<=end:
     mid = (start + end)//2
     if mylist[mid] == s:
         found = True
     elif s>mylist[mid]:
         start = mid + 1
     else:
         end = mid - 1

if found == False:
    print("not found")
else:
    print("found at ", mid) 

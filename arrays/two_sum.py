from array import *
arr = array('i',[4,2,3,7])
target = 5
dict_val = {}
for i in arr:
    found = target -i
    if found in dict_val:
        print(found,i)
        break
    dict_val[i] = "true"
    

        
           
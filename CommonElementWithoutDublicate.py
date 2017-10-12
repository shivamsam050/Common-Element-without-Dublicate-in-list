def Find(n):
    for i in range(n):
        if(list1[i] in list2 not in list1):
            list3.append(list1[i])
    print(list3)

list1 = [1,2,3,4,5,6,7,8]
list2 = [2,3,4,5,0]
list3 =[]
if(len(list1)>len(list2)):
    Find(len(list1))
else:
    Find(len(list2))    

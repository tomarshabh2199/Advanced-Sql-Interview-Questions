# List Comprehension Dictionary Comprehension
#set or Generator Comprehension

list_1=[1,32,4,5,45,,4,4,3,3,3,5,6,3,5,6,343]

divide_by_3=[]
for item in list_1:
    if item%3==0:
        divide_by_3.append(item)

print('Without using list comprehension',divide_by_3)
print('using list comprehension', [item for item in list_1 if item%3==0])

dict1={'a':45,'b':65,'A':56}
print({k.lower():dict1.get(k.lower(),0) + dict.get(k.upper(),0) for k in dict1.keys()})
 


squared={x**2 for x in {1,2,3,4,4,4,4,5,6}}
print(squared)

gen=(i for i in range(56) if i%3==0)
for item in gen:
    print(gen)
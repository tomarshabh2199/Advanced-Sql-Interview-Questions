#Map Function

#map(function_to_apply, list of inputs)

h1=[1,2,4,5,7]
sq=[]

def square(n):
    return n**2

for item in h1:
    sq.append(item**2)

sq=list(map(square,h1))
print(sq)


def greater_than_2(n):
    if n>2:
        return True
    else:
        return False

h1=[1,2,3,4,5,6,7,8]
greater_th_2=list(filter(greater_than_2, h1))
print(greater_th_2)



from functools import reduce

def sum_num(a,b):
    return a+b

li1=reduce(sum_num,[1,2,3])
print(li1)
















 
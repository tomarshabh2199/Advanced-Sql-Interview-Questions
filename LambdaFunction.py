lambda argument:manipulate(argument)

def add(a,b):
    s=a+b
    return s
print(add(6,4))

#one line function
add=lambda x,y:x+y
print(add(6,4))

a=[(1,2),(4,5),(555,34)]
a.sort(key=lambda x:x[1])
print(a)
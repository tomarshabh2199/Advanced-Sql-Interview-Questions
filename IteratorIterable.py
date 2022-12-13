# Iterator, Iterable, Iterator

def gen(n):
    for i in range(n):
        yield i


ob1=gen(1000000)
print(next(ob1))
print(next(ob1))



print(gen(1000000000))

for i in gen(1000):
    print(i)

for i in range(1000000):
    print(i)

#i nt object is not iterable
#string object is iterable


num="harry"
iter1=iter(num)
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))

import bisect
#it will tell index where we can insert that element so that our list will be sorted
number=5
a=[1,23,32,12,45]
print(a)
print(bisect.bisect(a, number))


#to insert that number
bisect.insort(a,number)

print(a)
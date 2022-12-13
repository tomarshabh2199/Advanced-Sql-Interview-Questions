import numpy as np
arr=np.arange(100000)
pythlist=list(range(10000))
%time for _ in range(10):[item*3 for item in pythlist]

%time for _in range(10): arr=arr*3

np.array([1,3,4,5,7,9])

array1=np.array([3,2,5,7,0],[1,12,4,3,7])
print(array1)

array1.shape

array1.dtype


np.zeros(4)

np.zeros((4,6))

np.ones(6).dtype

np.empty((4,6))

array1

array1*array1
array1/array1
array1**array1
1/array1

np.array(12**12)


array1.sum(axis=0)

array1.dot(array1)
array1.dot(array1.transpose())

dir(np)
len(dir(np))
np.cross(array1,array1)
np.sort(array1)
np.sort(array1,axis=0)


%%time
np.sort(array1, axis=0, kind='quicksort')


array1.reshape

array1

array1.shape

#gives the index to eleement to sort
np.argsort(array1)



#argsort- min element it will give
np.argmin(array1)


#argsort-max element it will give

np.argmax(array1)
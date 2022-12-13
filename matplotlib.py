#%matplotlib inline
from matplotlib import pyplot as plt
plt.plot([1,2,3],[2,5,7])
plt.title("Shubham Data")
plt.xlabel("this is x label")
plt.ylabel("this is y label")
plt.show()



from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')
x=[1,5,4]
y=[23,45,89]
x2=[3,7,3]
y2=[5,8,9]

plt.plot(x,y,label='first',linewidth='15')
plt.plot(x2,y2,label='second')
plt.hist(x2,y2,label='second')
plt.legend()
plt.show()
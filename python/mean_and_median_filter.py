
import numpy as np
import matplotlib.pyplot as plt
windowsize=5   #windowsize

def mean_cal(a):
    x=0
    for i in range(0,windowsize):
        x=x+a[i]
    return x/windowsize 


def median_cal(x):
    for i in range(0,windowsize):
        for j in range(i+1,windowsize):
            if(x[i]>x[j]):
                tmp=x[i]
                x[i]=x[j]
                x[j]=tmp
    return x[2]

mean=[]
median=[]

my_list = list(
    map(
        int,
        input('Enter space-separated integers: ').split()
    )
)
print(my_list)
for i in range(0,len(my_list)-(windowsize-1)):
    a=my_list[i:i+windowsize]
    output=median_cal(a)
    median.append(output)
    a=my_list[i:i+windowsize]
    output=mean_cal(a)
    mean.append(output)

# create x-axis
x_orin=list(range(0,len(my_list)))
x_new=list(range(0,len(my_list)-(windowsize-1)))

fig=plt.figure(num=1)
plt.plot(x_orin,my_list,'s-',color='r')
plt.title("original data")
fig2=plt.figure(num=2)
plt.plot(x_new,median,'s-',color='g',label="median")    #方形標記
plt.plot(x_new,mean,'o-',color='r',label="mean")        #圓形標記
plt.legend(
    loc='best',
    fontsize=20,
    shadow=False,
    #facecolor='#ccc',
    #edgecolor='#000',
    #title_fontsize=20
    )
plt.title("windowed data")
plt.show()
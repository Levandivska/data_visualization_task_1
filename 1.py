#!/usr/bin/python

import datetime as dt
import matplotlib.pyplot as plt
import csv as csv
import numpy as np

#Land-Ocean: Global Means
#Year,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec,J-D,D-N,DJF,MAM,JJA,SON

reader = csv.reader(open("data.csv","r"),delimiter=',')

X=[]
Y=[]
counter=0
for row in reader:
        print(int(row[0]),float(row[13]))
        X.append(int(row[0]))
        Y.append(float(row[13]))
        counter+=1 
print(counter)




fig,ax = plt.subplots()
ax.plot(X,Y, '.')
ax.grid(axis='x',color='0.95')
ax.grid( axis='y',color='0.95')
plt.title('Зміна температури поверхні відносно до середньої на кінець XIX сторіччя')
plt.text(1900,Y[X.index(1900)],'1900')
plt.text(1917,Y[X.index(1917)],'1917')
plt.text(1939,Y[X.index(1939)],'1939')
plt.text(1961,Y[X.index(1961)],'1961')
plt.text(1970,Y[X.index(1970)],'1970')
plt.text(1991,Y[X.index(1991)],'1991')
plt.text(2000,Y[X.index(2000)],'2000')
plt.text(2012,Y[X.index(2012)],'2012')

ax.set(xlabel='Рік.',ylabel='Відхилення температури, град.')
plt.show()



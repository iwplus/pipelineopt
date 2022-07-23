import numpy as np
import pandas as pd
print ()
print ("Jaringan dengan diameter dan Cost")
print ()
#pemasangan simpul dan harga ke dalam matriks bobot
bobot=[[152,49.54],
       [203,63.32],
       [254,94.82],
       [305,132.87],
       [356,170.93],
       [407,194.88],
       [458,232.94],
       [509,264.10]]

#pengombinasian 40 lintasan yang tiap lintasanya terdiri dari 5 simpul beserta total harga
camlin=[]
price=[]
for i in range(32768):
    lint=[]
    for i in range(5):
        lint.append(bobot[np.random.randint(len(bobot))])
    camlin.append(lint)
    harga=0
    for i in range(5):
        harga+=lint[i][1]*1000
    price.append(harga)

#membuat hasil kombinasi menjadi dataframe yang mudah dibaca
lintasan=[]
for j in range(len(camlin)):
    sublin=[]
    for k in range(5):
        sublin.append(camlin[j][k][0])
    sublin.append(price[j])
    lintasan.append(sublin)
#(*)CEK UPDATE
print(pd.DataFrame(lintasan,
                   columns=['node 1','node 2','node 3',
                            'node 4','node 5','harga'],
                   index=['kom %s'%(i+1) for i in range(len(lintasan))]))
print ()
print ("Urutan Jaringan dari harga yang paling Optimal")
print ()
#(*)UPDATE!!! pengurutan pola berdasarkan harga dari yang termurah ke yang termahal
lintasan=pd.DataFrame(lintasan,
                   columns=['node 1','node 2','node 3',
                            'node 4','node 5','harga'],
                   index=['kom %s'%(i+1) for i in range(len(lintasan))])
print(lintasan.sort_values(by=['harga']))
from math import exp
import os, pprint
pp=pprint.PrettyPrinter() # we'll use this later.

from  epanettools.epanettools import EPANetSimulation, Node, Link, Network, Nodes, Links, Patterns, Pattern, Controls, Control # import all elements needed
import random
from epanettools.examples import simple # this is just to get the path of standard examples

file = os.path.join('5 pipes.inp') # open an example
es=EPANetSimulation(file)
print(len(es.network.nodes))

n=es.network.nodes
es.run()
a=['1','2','3','4','5','6']
print()
totharga_s=0
p1=[0,164.654,162.054,160.321,159.454,158.588]
d2=[64.500,10.000,11.500,13.000,15.000,30.000]
min_p1=[150,150,150,150,150,150]
min_d2=[0,20.00,23.00,26.00,30.00,30.00]

penalty=0
for z in range (len(a)):
    if p1[z]<=min_p1[z] or d2[z]<=min_d2[z]:
        totharga_s+=1000        
print (f"Harga total setelah kena penalty = ",totharga_s)


print ("Changing Network____________________________________________")
import numpy as np
import pandas as pd

bobot=[[152,49.54],
       [203,63.32],
       [254,94.82],
       [305,132.87],
       [356,170.93]]

camlin=[]
price=[]
for i in range(1):
    lint=[]
    for i in range(5):
        lint.append(bobot[np.random.randint(len(bobot))])
    camlin.append(lint)
    harga=0
    for i in range(5):
        harga+=lint[i][1]*1000
    price.append(harga)

print()

print('Desain Jaringan setelah di Random (dirubah) = ',lint)

print()

d=Link.value_type['EN_DIAMETER']
print("Diameter sebelum dirubah")
for i in range (5):
    print(es.ENgetlinkvalue(i+1,d)[1])
#print (es.network.links[2].results[d]) # new interface
for i in range (5):
    
#print ()
    r=es.ENsetlinkvalue(i+1,d,lint[i][0]) # now let's change values - link

print("Diameter setelah dirubah")
for i in range (5):
    print(es.ENgetlinkvalue(i+1,d)[1])

print()
print()

# to permanantly change values, the changed network has to  be written to a new file
import tempfile, os
f=os.path.join("te.inp")
es.ENsaveinpfile(f) # save the changed file
file_2 = os.path.join('te.inp') # open an example
e2=EPANetSimulation(file_2)
print(len(e2.network.nodes))

e2.run()

print('PRESSURE')
p=Node.value_type['EN_PRESSURE']
a=['1','2','3','4','5','6']
for i in range(len(a)):
    print (f"Pressure Node {i+1} = ","%4.2f" %e2.network.nodes[a[i]].results[p][6])

print()
print('DEMAND')
d=Node.value_type['EN_DEMAND']
for j in range(len(a)):
    print (f"Demand node {j+1} = ","%4.2f" %e2.network.nodes[a[j]].results[d][6])

print()
print()

totharga=0
penalty=0
for i in range(5):
    if e2.network.nodes[a[i]].results[p][6]<=min_p1[i] or e2.network.nodes[a[i]].results[d][6]<=min_d2[i]:
        penalty+=1000
              
    harga1 = bobot[i][1] #Tugas totharga yang ditambah penalty

    l1 = es.ENgetlinkvalue(i+1,d)[1]
    f=l1*harga1
    totharga+=f
    #print(f'@Harga pipa {i+1} adalah {harga1} dengan panjang {l1}. Sehingga biaya pipa {i+1} adalah {f}')
 
totharga+=penalty
print ()
print('Total biaya Jaringan 2 : ',totharga)

print()


t=1
alpha=0.1
beta=0.0001
min_p1=[150,150,150,150,150,150]
min_d2=[0,20.00,23.00,26.00,30.00,30.00]

s=[[356, 170.93], [305, 132.87], [254, 94.82], [254, 94.82], [356, 170.93]]
list(s)
print('Jaringan awal :')
print()
print(list(s))
print()
  
while t>=beta:
    
  #totharga_s1=totharga
  
  s_1=s
    
  ind1=random.randint(0,len(s)-1)
  ind2=random.randint(0,len(s)-1)
  print(ind1)
  print(ind2)
  temp=[]  
  temp=s_1[ind1]
  s_1[ind1]=s_1[ind2]
  s_1[ind2]=temp
  print('Jaringan setelah di tukar  :')
  print()
  print(s_1)
  d=Link.value_type['EN_DIAMETER']
  print("Diameter sebelum dirubah")
  for i in range (len(s)):
      print(es.ENgetlinkvalue(i+1,d)[1])
  #print (es.network.links[2].results[d]) # new interface
  for i in range (len(s)):
    
  #print ()
      r=es.ENsetlinkvalue(i+1,d,s_1[i][0]) # now let's change values - link

  print("Diameter setelah dirubah")
  for i in range (len(s)):
      print(es.ENgetlinkvalue(i+1,d)[1])

  print()
  print()

  # to permanantly change values, the changed network has to  be written to a new file
  import tempfile, os
  f=os.path.join("te.inp")
  es.ENsaveinpfile(f) # save the changed file
  file_2 = os.path.join('te.inp') # open an example
  e2=EPANetSimulation(file_2)
  print(len(e2.network.nodes))

  e2.run()

  print('PRESSURE')
  p=Node.value_type['EN_PRESSURE']
  d=Node.value_type['EN_DEMAND']
  a=['1','2','3','4','5','6']
  penalty=0
  for i in range(len(a)):
      if e2.network.nodes[a[i]].results[p][6]<=min_p1[i] or e2.network.nodes[a[i]].results[d][6]<=min_d2[i]:
          penalty+=1000
              
  totharga_s1=0
  for m in range(len(s)):
      harga1 = s_1[m][1]

      l1 = es.network.links[m+1].results[d]
      l1 = l1[0]
      f=l1*harga1
      totharga_s1+=f
  
  totharga_s1+=penalty
  print ()
  print('Total biaya Jaringan yang ditukar (s1): ',totharga_s1)        
  delta=totharga_s1-totharga           
  if delta <0:
    s=s_1
    totharga=totharga_s1
  else:
    r=np.random.normal(1)
    p=exp(-delta/t)
    if r<=p:
        s=s_1
        totharga=totharga_s1
  t=alpha*t
    
print('Total biaya Jaringan: ',totharga)
print('Jarigan: ',s)

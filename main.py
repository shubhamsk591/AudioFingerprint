import ast
import csv
import os
import numpy as np
import fingerprint as fp
from numpy import linalg
import fingerprint as f
import math
def get_value_from_index(index): 
	# open the csv file 
	with open('features_db.csv', 'r') as csvfile: 
		# read the csv file 
		csvreader = csv.reader(csvfile) 
		# get all the rows in the csv file 
		rows = list(csvreader) 
		# return the value from the specified index 
		return rows[index][1] 
def euclidien_distance(x,x1,y,y1):
    sum=0
    n=len(x)
    for i in range(n):
        sum = math.sqrt(math.pow(x[i] - x1[i], 2) + math.pow(y[i] - y1[i], 2))
        sum=sum+sum
    return sum/n
def cosine(x,x1,y,y1):
    

    cosine = np.dot(x,x1)/(np.linalg.norm(x)*np.linalg.norm(x1))
    cosine1 = np.dot(y,y1)/(np.linalg.norm(y)*linalg.norm(y1))
    return cosine,cosine1

def split(x,tx,ty):
    n1=int(len(tx)/len(x))
    x1=[[0]*len(x)]*n1
    y1=[[0]*len(x)]*n1
    x1= np.array(x1)
    y1= np.array(y1)
    c1=0
    for i in range(n1):
        for j in range(len(x)):
            x1[i][j]=tx[c1]
            y1[i][j]=ty[c1]
            c1=c1+1
    return x1,y1
def slide(x,tx,ty):
    n1=len(tx)-len(x)
    n1=n1+1
    x1=[[0]*len(x)]*n1
    y1=[[0]*len(x)]*n1
    x1= np.array(x1)
    y1= np.array(y1)
    for i in range(n1):
        c1=i
        for j in range(len(x)):
            x1[i][j]=tx[c1]
            y1[i][j]=ty[c1]
            c1=c1+1
    return x1,y1

def readlist(reader):
    n=len(reader)
    listh=[]
    for i in range(1,n):
        t=int(reader[i][3])
        list=[]
        for j in range(4,t+4):
            list.append(reader[i][j])
        listh.append(list)
    return listh

with open('features_db.csv', 'r') as csvFile:
        reader = list(csv.reader(csvFile))
s=readlist(reader)
x1=[]
y1=[]
for i in range(len(s)):
    n=len(s[i])
    x=[]
    y=[]
    for j in range(n):
        len1=ast.literal_eval(s[i][j])
        x.append(int(len1[0]))
        y.append(int(len1[1]))
    x1.append(x)
    y1.append(y)

song_files = os.listdir('test/')
for file in song_files:
   file_name="test/"+file
   features = f.fingerprint(file,file_name)
   x=np.array(features[0])
   y=np.array(features[1])
   resulte=[]
   resultcs=[]
   for i in range(len(x1)):
       tx=np.array(x1[i])
       ty=np.array(y1[i])
       splittx,splitty=slide(x,tx,ty)
       vectored=[]
       vectorcs=[]
       for r in range(len(splittx)):
           vectored.append(euclidien_distance(splittx[r],x,splitty[r],y))
           vectorcs.append((cosine(splittx[r],x,splitty[r],y)))

       resulte.append(min(np.array(vectored)))
       resultcs.append(max(vectorcs, key=lambda x:x[1]))
   output=[]
   print("Using Euclident Distance")
   for j in range(len(resulte)):
    if(resulte[j]<100):
        output.append([j+1,resulte[j]])
   output.sort(key = lambda x : x[1])
   for i in range(len(output)):
    print(get_value_from_index(output[i][0]))
   print("\n")
   output=[]
   print("Using  cosine")
   for j in range(len(resultcs)):
    z=resultcs[j]
    z=z[1]
    if(z>0):
        output.append([j+1,z])
   output.sort(key = lambda x : x[1],reverse=True)
   for i in range(len(output)):
    print(get_value_from_index(output[i][0]))
   print("\n")
   output=[]
   print("Using  cosine x")
   for j in range(len(resultcs)):
    z=resultcs[j]
    z=z[0]
    if(z>0):
        output.append([j+1,z])
   output.sort(key = lambda x : x[1],reverse=True)
   for i in range(len(output)):
    print(get_value_from_index(output[i][0]))
   print("\n")

           
           


    


    

        
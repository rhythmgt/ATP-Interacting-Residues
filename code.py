# -*- coding: utf-8 -*-
"""IQB-A3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12au_vbi9pcPb8-ZTcQuPzuGlBz3i_ISp
"""

import numpy as np 
import pandas as pd 
df = pd.read_csv("train.data")
print(df)

def strip(a):
    lim = len(a)
    padding = "X"*8
    a = padding + a + padding
    ans = []
    label = []
    for i in range(lim):
        
        if (a[i+8].islower()):
            label.append(1)
        else:
            label.append(-1)
        ans.append(a[i:i+17])
    return(ans, label)
        
aa = ["G", "A", "L", "M", "F", "W", "K", "Q", "E", "S", "P","V","I", "C", "Y","H", "R", "N", "D", "T","X"]

def binprof(a):
    temp = []
    for i in range(len(a)):
        for j in range(len(aa)):
            if (a[i] == aa[j]):
                temp.append(1)
            else :
                temp.append(0)
    
    return (temp)

import datetime
now = datetime.datetime.now()
print ("Start date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

seq = []
label = []
xval = []
numseq = 0
for i in df['Amino Acid Sequence']:
    numseq+=len(i)
    se, lab = strip(i)
    for j in se:
        k = binprof(j.upper())
        xval.append(k)
    seq.extend(se)
    label.extend(lab)

scores = []
x = pd.DataFrame() 
x["Sequence"] = seq

for i in range(17):
    for j in range(len(aa)):
        k = [row[(i*len(aa))+ j] for row in xval]
        x[str(i) + aa[j]] = k 

y = pd.DataFrame()
y["label"] = label
x["label"] = label

x.drop(inplace = True, columns = ["Sequence"])
print(x)
print(y)

x.drop_duplicates(keep='first', inplace= True)
x.shape
y = x['label']
x.drop(inplace = True, columns = ["label"])
print(x)
print(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn import svm

clf = svm.SVC(kernel = 'rbf', gamma = 'auto', class_weight='balanced')

clf.fit(X_train, y_train.values.ravel())

y_out = clf.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test, y_out))

print(classification_report(y_test, y_out))

tst = pd.read_csv("test1.txt")
print(tst)

inp = ''
for i in tst['Lable']:
  inp += i
print(inp)

seq2 = []
xval2 = []
numseq = 0
se, lab = strip(inp)
for j in se:
  k = binprof(j.upper())
  xval2.append(k)
seq2.extend(se)

tx = pd.DataFrame() 
tx["Sequence"] = seq2

for i in range(17):
    for j in range(len(aa)):
        k = [row[(i*len(aa))+ j] for row in xval2]
        tx[str(i) + aa[j]] = k 


tx.drop(inplace = True, columns = ["Sequence"])
ty = clf.predict(tx)

cnt = 0
for k in ty:
  if (k==1):
    cnt+=1
print(cnt)

tst.drop(inplace = True, columns = ["Lable"])
tst["Lable"] = ty
print(tst)

tst.to_csv("output.csv", index=False)
end= datetime.datetime.now()
print ("End date and time : ")
print (end.strftime("%Y-%m-%d %H:%M:%S"))

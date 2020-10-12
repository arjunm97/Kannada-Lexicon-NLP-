# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 23:13:29 2019

@author: Arjun
"""
#Noun inflectional generator

word=""
import pandas as pd

df = pd.read_excel (r'noun_rules.xlsx') 
print (df)

words=["ಹುಡುಗ","ಅಣ್ಣ","ಕಮಲಾ","ಅಕ್ಕ","ಮರ","ಚಿಕ್ಕ","ಕವಿ","ಗೌರಿ","ತಾಯಿ","ಗುರು","ಹೆಣ್ಣು","ತಂದೆ"]


##SQL code for retriving the word from database:

df2=pd.read_csv(r"lexicon.csv")
print(df2)
X = df2.iloc[:, 0].values
Y = df2.iloc[:, 3].values
x=list(X)
y=list(Y)


#GUI for taking input

import tkinter as tk

def get_class():  #no need to pass arguments to functions in both cases
    print (var.get())

def get_entry(): 
    print (ent.get())


root = tk.Tk()

var = tk.StringVar()
cate=tk.StringVar()#category
gend=tk.StringVar()#gender


ent = tk.Entry(root,textvariable = var)
cat=tk.Entry(root,textvariable = cate)
gen=tk.Entry(root,textvariable = gend)
btn1 = tk.Button(root, text="Enter details", command=get_class)

ent.pack()
cat.pack()
gen.pack()
btn1.pack()


root.mainloop()

word=var.get()
category=cate.get()
gender=gend.get()

#print(word,category,gender)
z = x.index(word)
category=y[z]#Change here when sql database is available
o = category[0]
print(category)
o = int(o)
#####Got the word,category
df.reset_index(inplace=True)
p=df.loc[ o , : ]
p=list(p)
print(p)
p.pop(0)
p.pop(0)
p.pop(0)

print(p)

inflex_morh=list()
for i in p:
    new_word=word+i
    inflex_morh.append(new_word)
    
print(inflex_morh)    

print(*inflex_morh, sep = "\n") 




# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:56:11 2019

@author: USER
"""
import pandas as pd
wo = input("Enter")
df = pd.read_excel (r'noun_rules.xlsx') 
df2=pd.read_csv(r"lexicon.csv")
X = df2.iloc[:, 0].values
Y = df2.iloc[:, 3].values
x=list(X)
y=list(Y)
z = x.index(wo)
category=y[z]#Change here when sql database is available
o = category[0]
o = int(o)
	#####Got the word,category
df.reset_index(inplace=True)
p=df.loc[ o , : ]
p=list(p)
print(p)
p.pop(0)
p.pop(0)
p.pop(0)

	

inflex_morh=list()
for i in p:
    new_word=wo+i
    inflex_morh.append(new_word)
    
print(inflex_morh)
	
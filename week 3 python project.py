#!/usr/bin/env python
# coding: utf-8

# In[3]:


#importing the necessary libraries
import random
import math

#random command for the program to assign a random value at the beginning of the game
x=random.randint(1,100)

#interface with the user of the game
print('\n\t You have only',round(math.log(100-1+1,2)),'chances to guess the number\n' )

#initializing the counting 
count=0

#count command for limiting the number of times to play
while count<math.log(100-1+1,2):
    count +1
    
   #guess input 
    guess=int(input('Guess a number between 1 and 100: '))
    
   
   
        
    #looping to compare the user input and the randomly generated value and give the response    
    
    if x== guess:
        print('Congratulations you did it in', count,'try' )
        break
        
        
    elif x > guess:
            print('You guessed too small!')
            
            
    elif x < guess:
                print('You guessed too high!')
            
#termination of the game incase number of trials are exceeded
                
if count>= math.log(100-1+1,2):
                    print('\n The number is  ', x)
                    print('\t Better luck next time!')
            
                    break


# In[15]:


#exploratory Data analysis of a sales dataset 


#importing libraries
import statistics
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

#importing the file
dataframe=pd.read_csv('sales_data_sample.csv',encoding='unicode_escape')
df=dataframe.head(20)
print(df)

#information on the data
dataframe.info()
dataframe.describe()
# x=df.isnull().sum()
# print(x)\

#dropping null values
newdf=df.dropna()
print(newdf.to_string())

#visualization of data
x=newdf['COUNTRY']
y=newdf['SALES']


#plotting a histogram
plt.hist(x,y)
plt.show()

#plotting a bar graph
plt.barh(x,y)
plt.show() 

#plotting a scatter plot
plt.scatter(x, y)
plt.show()  

#plotting a table plot
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.show()

#calculating statistical insights
statistics.mean(newdf['SALES'])

statistics.median(newdf['SALES'])
statistics.stdev(newdf['SALES'],newdf['PRICEEACH'])


# In[ ]:





# In[ ]:





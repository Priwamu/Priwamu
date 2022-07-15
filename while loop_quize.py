#!/usr/bin/env python
# coding: utf-8
 Challenge : 
    
    
q1 : Try to print this by using while loop 
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * 

q2 : try to print below by using while loop : 
        
A
B H 
C I N
D J o S
E K p T W
F L Q U X z
G M R V Y 

q3 : Try to print all the number divisible by 3 in between a range of 40 - 400
    
q4 : Try to filter out all the vowels form below text by using while loop : 
 """Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[36]

Python consistently ranks as one of the most popular programming languagesc""" 


q5 : Try to generate all the even number between 1- 1000

q6 : Define a function for all the above problem statememnt  . 
    
q7 : write a code to get a time of your system 

q8 : Write a code to fetch date form your system 

q9 : Write a code to send a mail to your friend 

#q9 : Write a code to send a mail to your friend 

q11 : write a code to check ip address of your system 

q12 : Write a code to check a perticular installation in your system

q13 : Write a code to convert any text in to voice 

q14 : you have to write a fun which will take string and return a len of 
it without using a inbuilt fun len

q15 :write a fun which will be able to print an index of all premitive element which you will pass 

q16 : Write a fun which will take input as a dict and give me out as a list of all the values 
even in case of 2 level nesting it should work . 

q17 : write a function whihc will take multiple list as a input and give me concatnation of all the element as 
and output

q18 : Write a function which will whould return list of all the file name from a directory . 

q19 : write a function whihc will be able to read a image file and show it to you .
    
q20 : write a function by which you will be able to append two PDF files . 
    
q21 : write a function which can help you to filter only word file from a directory . 
    
q22 : write a function which can read video file and play for you . 
    
q23 : write a function which will be able to shutdonw your system . 

q24 : Write a function which will whould return list of all the file name from a directory . 

q25 : write a function whihc will be able to access your mail . 
        
# In[ ]:


#q1 : Try to print this by using while loop 
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * 


# In[2]:


i=9
n=1
while n<=i:
    print(' *' *n)
    n=n+1


# In[ ]:


#q2 : try to print below by using while loop : 
        
A
B H 
C I N
D J o S
E K p T W
F L Q U X z
G M R V Y 


# In[11]:


x=0           # work with chr(character.)
while x<8:
    content=''
    y=0
    while y<x:
        z=0
        sum=0
        while z<y:
                sum+=6-z
                z+=1
        if(x+64+sum)<=(64+26):
                 content+=" " + chr(x+64+sum)
        y+=1
    print(content)
    x+=1


# In[14]:


chr(65)


# In[16]:


i=0
while i<7:
    print(i)
    c=65+i
    print(c)
    j=0
    print(j)
    while j<(i+1):
        if c==91:
            break
        print(chr(c),end=" ")  # print c which is A
        c=c+6-j # element to skip
        print(c)
        j+=1
        print(j)
    i+=1
    print(i)
    print()
        


# In[19]:


i=0
while i<7:
    c=65+i
    j=0
    while j<(i+1):
        if c==91:
            break
        print(chr(c),end=" ")  # print c which is A
        c=c+6-j # element to skip
        j+=1
    i+=1
    print()
        


# In[21]:


##q3 : Try to print all the number divisible by 3 in between a range of 40 - 400
i=40
while i<=400:
    if i%3==0:
        print(i)
    i=i+1
    


# In[22]:


#q4 : Try to filter out all the vowels form below text by using while loop : 
s= """Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[36]

Python consistently ranks as one of the most popular programming languagesc""" 


# In[23]:


i=0
v='aeiou'
# convert everything to lowercase
s=s.lower()
while i < len(s):
    if s[i] in v:
        print(s[i])
    i=i+1


# In[24]:



#q5 : Try to generate all the even number between 1- 1000

i=1
while i<=1000:
    if i%2==0:
        print(i)
    i=i+1


# In[25]:


#q6 : Define a function for all the above problem statememnt  
def vowel(s):
    i=0
    v='aeiou'
# convert everything to lowercase
    s=s.lower()
    while i < len(s):
        if s[i] in v:
            print(s[i])
        i=i+1
   


# In[26]:


vowel(s)


# In[27]:


# q7 : write a code to get a time of your system 
import datetime
datetime.datetime.now().time()


# In[28]:


#q8 : Write a code to fetch date form your system
import datetime
datetime.date.today()


# In[ ]:


#q9 : Write a code to send a mail to your friend 
import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login('****@gmail.com','****')

server.sendmail('****@gmail.com','Test Email from python')

print('Mail sent')


# In[ ]:


# write a code to trigger alarm for you at a scheduled time
import time
import playsound

alarm_time='10.22'
if time.asctime()[11:8]==alarm_time:
    absolute_path=os.path.abspath('textovoice.mp3')
    print(absolute_path)
    playsound.playsound(absolute_path)


# In[41]:


#q11 : write a code to check ip address of your system 

import socket
host=socket.gethostname()
ip=socket.gethostbyname(host)
print('your ip adress is:',ip)
print('your computer name is:',host)


# In[50]:


#q12 : Write a code to check a particular installation in your system

get_ipython().system('pip install winapps')


# In[ ]:


#q13 : Write a code to convert any text in to voice 
import gtts
from playsound import playsound
def txt_to_voice(str1):
    tts=gtts.gTTS(str1)
    tts.save('Hello.mp3')
    playsound('Hello.mp3')
text=input("Enter the text to convert to voice")
txt_to_voice(Text)


# In[ ]:





# In[53]:


#q14 : you have to write a fun which will take string and return a len of 
#it without using a inbuilt fun len

s='prisci'
len(s)


# In[54]:


def str_len(s):
    count=0
    for i in s:
        count=count+1
    return count


# In[55]:


str_len('dfghy')


# In[56]:


#q15 :write a fun which will be able to print an index of all premitive element which you will pass 

def print_prim(l):
    for i in range(len(l)):
        print(i)


# In[59]:


print_prim([1,3,4,5," wamjr",[3,6,7,8,4]])


# In[60]:


# q16 : Write a fun which will take input as a dict and give me out as a list of all the values 
#even in case of 2 level nesting it should work . 
d={'k1':'value','k2':'value','k3':{"k12":'liz','k13':'gafasd'}}


# In[65]:


def dic_to_list(d):    # the function which will take input as dict and give out list of values
    l=[]
    for i in d.values():
        if type(i) !=dict:
            l.append(i)
        if type(i)==dict:
            for j in i.values():
                l.append(j)
    return l


# In[66]:


dic_to_list(d)


# In[70]:


#q17 : write a function which will take multiple list as a input and give me concatnation of all the element as and output
get_ipython().system('pip install opencv-python')


# In[10]:


import cv2

def read_img():
    a=cv2.imread('images/roger federer.jpg',1)
    cv2.imshow('myimg',a)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    


# In[11]:


read_img()


# #### READING,WRITING AND DISPLAYING IMAGES WITH OPENCV

# In[6]:


# import open cv library
import cv2


# In[7]:


import numpy as np


# In[4]:


import cv2
from matplotlib import pyplot as plt


# In[4]:


#load image using 'imread'specifying the path to image
import cv2
from matplotlib import pyplot as plt
img=cv2.imread('images/cow.jpg',0)
# to display image we use 'imshow' the first parameter is title shown on image window
# the second parameter is image variable
cv2.imshow('test_img',img)
# waitkey allows us to input information when the image is open
# by placing number except(0)we can specify for how long you keep the window open(time in milliseconds)
cv2.waitKey(5000)
#cv2.destroyallwindows() closes all open windows,failure to place this will cause your program to hang
cv2.destroyAllWindows()


# In[ ]:


import cv2
from matplotlib import pyplot as plt
img1=cv2.imread('images/messi.jpg',1)
cv2.imshow('test_img', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[6]:


img=cv2.imread('images/cow.jpg',0)
plt.imshow(img)


# In[ ]:





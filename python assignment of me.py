#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("twinkle, twinkle, little star,")
print("      how i wonder what you are!")
print("            Up above the world so high,")
print("            Like a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("      How I wonder what you are")


# In[5]:


from datetime import datetime

now = datetime.now()

print("now = ", now)

dt_string = now.strftime("%d/%m/%Y %H :%M:%S")
print("date and time =", dt_string)


# In[11]:


num1 = 1.5
num2 = 6.3
sum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# In[12]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[13]:


import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[14]:


from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# In[ ]:





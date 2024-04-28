#!/usr/bin/env python
# coding: utf-8

# 
# # Tuples
# 

# 
# * Tuples are denoted by parentheses ( ).
# 
# 

# * Like lists, tuples can contain items of different data types, such as integers, strings, or even other tuples.
# 

# 
# * Tuples are immutable, meaning once created, their elements cannot be changed, added, or removed.

# * You can access elements in a tuple using indexing, starting from 0 for the first element.
# 
# 

# * Tuples support various operations such as slicing, concatenation, and repetition.
# 
# 

# * They are commonly used for representing fixed collections of items, such as coordinates or database records.
# 
# 

# * Tuples are often used in situations where immutability and integrity of data are desired.
# 
# 

# * Tuples are iterable, allowing you to loop through their elements using loops like for or tuple unpacking.
# 
# 

# * Although tuples are immutable, they can contain mutable objects like lists, meaning you can modify the elements within a mutable object contained in a tuple, but you can't modify the tuple itself.

# ## Let's Start

# In[1]:


tuples = (1, "sweta", "bishnu", 2)
print(tuples)


# ## Tuples also allow duplicate

# In[5]:


tuples = (1, "sweta", "bishnu", 2, 2, 2)
print(tuples)


# ## Length of the tuples

# In[6]:


tuples = (1, "sweta", "bishnu", 2, 2, 2)
print(len(tuples))


# For one item in tuples we should keep comma
# 

# In[7]:


tuples = ("is_tuples",)
print(type(tuples))


# In[8]:


tuples = ("not_tuples")
print(type(tuples))


# ## typecasting tuple 

# In[9]:


list = [1,"ishu", "nunu" , 11.34]
print(tuple(list))


# ## Accessing the elements in the tuples 
# 
# [start:stop:step]

# In[14]:


tuples = (1,"ishu", "nunu" , 11.34)
print(tuples[0]) 


# In[15]:


tuples = (1,"ishu", "nunu" , 11.34)
print(tuples[-1])


# In[18]:


tuples = (1,"ishu", "nunu" , 11.34, "sweta", "bishnu" , "suraj", "sopu")
print(tuples[2:4])


# In[20]:


tuples = (1,"ishu", "nunu" , 11.34, "sweta", "bishnu" , "suraj", "sopu")
print(tuples[:2])


# In[21]:


tuples = (1,"ishu", "nunu" , 11.34, "sweta", "bishnu" , "suraj", "sopu")
print(tuples[2:])


# In[22]:


tuples = (1,"ishu", "nunu" , 11.34, "sweta", "bishnu" , "suraj", "sopu")
print(tuples[::2]) 


# In[23]:


tuples = (1,"ishu", "nunu" , 11.34, "sweta", "bishnu" , "suraj", "sopu")
print(tuples[2::])


# In[24]:


tuples = (1,"ishu", "nunu" , 11.34, "sweta", "bishnu" , "suraj", "sopu")
print(tuples[-4:-1])


# USING if case
# 

# In[2]:


tuples = (1,"ishu", "nunu" , 11.34, "sweta", "bishnu" , "suraj", "sopu")
if "ishu" in tuples:
    print("Hello Ishu!")


# ## Updating Element in the list

# In[1]:


tuples = ("A", "B", "C", "D", "E")
#first of all to update we have
lists = list(tuples)
lists[0] = "Z"
print(lists)


# In[4]:


tuples = ("A", "B", "C", "D", "E")
#first of all to update we have
lists = list(tuples)
lists.append("Apple")
print(lists)


# In[11]:


tuples = ("A", "B", "C", "D", "E")
newtuples = ("F", "G", "H")
tuples += newtuples
print(tuples)


# ## Removing element from the tuple
# 

# In[8]:


tuples = ("A", "B", "C", "D", "E")
#first of all to update we have
lists = list(tuples)
del lists
print(lists)


# In[16]:


tuples = ("yellow", "blue", "black")
y = list(tuples)
y.remove("yellow")
tuples = tuple(y)
print(tuples)


# 
# * Packing tuples
# * Unpacking Tuple

# In[18]:


#packing tuples which means assignning value to tuples
tuples = ("yellow", "blue", "black")
print(tuples)


# In[27]:


#unpacking tuples, which means extracting values of tuples
Countries = ("Nepal", "USA", "Germany", "India", "New Zealand")
(coun1, coun2, coun3, coun4, coun5) = Countries
coun1
print(coun5)


# Using Asterisk

# In[24]:


Countries = ("Nepal", "USA", "Germany", "India", "New Zealand")
Countries = ("Nepal", "USA", "Germany", "India", "New Zealand")
(coun1, coun2, *countr) = Countries # here asterick is used for assigning all the remaning values
print(countr)


# In[28]:


Countries = ("Nepal", "USA", "Germany", "India", "New Zealand")

(coun1, *coun2, countr) = Countries # here asterick is used for assigning values after coun1 to to remaing values, except last one
print(coun2)


# joining the tuples

# In[32]:


countries = ("Nepal", "USA", "Germany", "India", "New Zealand")
add = ("London",)
newtuple = countries + add
print(newtuple)


# ## count function

# In[33]:


countries = ("Nepal", "USA", "Germany", "India", "New Zealand")
print(countries.count("Nepal"))


# In[35]:


countries = ("Nepal", "USA", "Germany", "India", "New Zealand")
lsit = list(countries)
print(lsit.index("Germany"))


# In[ ]:





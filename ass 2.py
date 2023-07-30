#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#python dictionary methods
#clear,copy,fromkeys,get,items,keys,pop,popitems,setdefault,update,values.


# In[1]:


sai ={"age":20,"year":2003,"place":"Hyderabad"}
sai.clear()
print(sai)


# In[2]:


sai={"age":20,"year":2003,"place":"Hyderabad"}
a =sai.copy()
print(a)


# In[3]:


sai={"age":20,"year":2003,"place":"Hyderabad"}
a =sai.get("place")
b =sai.get("age")
print(a)
print(b)


# In[4]:


sai={"age":20,"year":2003,"place":"Hyderabad"}
a =sai.items()
print(a)


# In[5]:


sai={"age":20,"year":2003,"place":"Hyderabad"}
a =sai.keys()
print(a)


# In[6]:


sai={"age":20,"year":2003,"place":"Hyderabad"}
sai.pop("place")
print(sai)


# In[7]:


sai={"age":20,"year":2003,"place":"Hyderabad"}
a=sai.popitem()
print(a)


# In[8]:


sai={"age":20,"year":2003,"place":"Hyderabad"}
a = sai.setdefault("palce","Chennai")
print(a)


# In[9]:


sai={"age":20,"year":2003,"place":"Hyderabad"}
sai.update({"height":5.9})
print(sai)


# In[10]:


sai={"age":20,"year":2003,"place":"Hyderabad"}
a = sai.values()
print(a)


# In[ ]:





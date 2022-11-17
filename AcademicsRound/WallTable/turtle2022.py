#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
import os
groupname="walltable"


# In[ ]:


import turtle
skk = turtle.Turtle()
 
skk.lt(90)
skk.fd(100)
skk.rt(90)
skk.fd(30)
skk.circle(-25,180)
skk.fd(15)
skk.rt(220)
skk.fd(75)

outputpath=os.path.dirname(os.path.abspath(__file__))+os.path.sep+groupname+'.ps'
skk.getscreen().getcanvas().postscript(file=outputpath)


# In[ ]:





# In[ ]:





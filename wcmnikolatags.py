
# coding: utf-8

# wcm Nikola Tags
# 
# convert ipynb/py doc imports as tags for nikola blog .meta files.
# 
# When user searches for notebook to blog with bbknikola python script also get the tags for the .meta file. Open up the .py file and convert this:
# 
# blogpost.py
# 
# import requests
# import os
# import re
# 
# Into:
# 
# blogpost.meta
# 
# blogpost
# blogpost
# 2015/02/31 00:00:00
# requests, os, re

# Categorie can be the name of the repo.
# Need a repo for Nikola scripts

# In[13]:

import os
from walkdir import filtered_walk, dir_paths, all_paths, file_paths


# In[14]:

nbog = raw_input('Name of notebook to tag: ')


# In[15]:

files = file_paths(filtered_walk('/home/wcmckee/github/', depth=100, included_files=[nbog + '.py']))


# In[16]:

print files


# In[17]:

for fil in files:
    #print fil
    opfil = open(fil, 'r')
    print opfil.read()
    opfil.close()


# In[19]:

opfilz = open(fil, 'r')

opfilz.read()


# In[1]:

#python module that can be used to scan .py files and return
#the imports as a list.


# In[ ]:




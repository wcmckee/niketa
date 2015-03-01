
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

# In[26]:

import modulefinder
import runpy
import os
from walkdir import filtered_walk, dir_paths, all_paths, file_paths


# In[22]:

mwcm = modulefinder.ModuleFinder()


# In[23]:

mwcm.any_missing()


# In[24]:

mwcm.run_script('/home/wcmckee/github/niketa/rgdsnatch.py')


# In[35]:

mwcm.path


# In[39]:

mwcm.scan_code


# In[10]:

from splinter import Browser
browser = Browser()


# In[11]:

browser.visit('http://google.com')


# In[12]:

browser.title


# In[9]:

browser.request_url


# In[15]:

#browser.click_link_by_href('http://www.google.co.nz/preferences')


# In[1]:

import time


# In[19]:

#Code for open up web browser on library system and 
#acceot their t&c.
#Need to get web address to go to, and button find_by_name 
#to click.

from splinter import Browser

with Browser() as browser:
    # Visit URL
    url = "http://www.google.com"
    browser.visit(url)
    browser.fill('q', 'artcontrol')
    # Find and click the 'search' button
    button = browser.find_by_name('btnG')
    # Interact with elements
    button.click()
    time.sleep(5)
    if browser.is_text_present('artcontrol.me'):
        print "Yes, the official website was found!"
    else:
        print "No, it wasn't found... We need to improve our SEO techniques"


# In[ ]:




# In[27]:

mwcm.report()


# In[28]:

runpy.run_module('requests')


# In[ ]:




# In[29]:

nbog = raw_input('Name of notebook to tag: ')


# In[30]:

files = file_paths(filtered_walk('/home/wcmckee/github/', depth=100, included_files=[nbog + '.ipynb']))


# In[35]:

#Easier to access ipynb and access the code import cell.
#Parse the notebook for import tags
#IPython module wrapper for returning list of imported modules
#from a ipynb file. 
#Get the list of modules for tags from this.


# In[32]:

for fil in files:
    #print fil
    opfil = open(fil, 'r')
    print opfil.read()
    opfil.close()


# In[33]:

opfilz = open(fil, 'r')

opfilz.read()


# In[34]:

#python module that can be used to scan .py files and return
#the imports as a list.


# In[ ]:




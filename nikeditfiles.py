
# coding: utf-8

# Nik Edit Files
# 
# Edit blog files

# In[64]:

import nikola

import dominate
from dominate.tags import * 
from time import gmtime, strftime
import time


# In[66]:

import os


# In[67]:

prodir = ('/home/wcmckee/sellcoffee/products/')


# In[68]:

prodlis = os.listdir('/home/wcmckee/sellcoffee/products/')


# In[69]:

#Display index.html page that has products list, price, sales
#etc.

prodlis


# In[70]:

#(prodir + rdz + '/' + rdz + '-price')


# In[70]:




# In[70]:




# In[ ]:

doc = dominate.document(title='BroBeur CyberCafe products')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type ='text/javascript', src='script.js')
    #str(str2)
    
    with div():
        attr(cls='header')
        h1('BroBeur CyberCafe products')
        h3('BroBeur CyberCafe Products')
        #p(img('imgs/getsdrawn-bw.png', src='imgs/getsdrawn-bw.png'))
        #p(img('imgs/15/01/02/ReptileLover82-reference.png', src= 'imgs/15/01/02/ReptileLover82-reference.png'))
        p('Updated ', strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        #p(panz)
        #p(bodycom)
    
    

with doc:
    with div(id='body').add(ol()):
        for rdz in prodlis:
            #h1(rdz.title)
            #a(rdz.url)
            #p(img(rdz, src='%s' % rdz))
            #print rdz
            #p(img(rdz, src = rdz))
            h3(rdz)
            oprdz = open((prodir + rdz + '/' + rdz + '-id'), 'r')
            p('id: ' + oprdz.read())
            oprdz.close()
            
            prrdz = open((prodir + rdz + '/' + rdz + '-price'), 'r')
            p('price: ' + prrdz.read())
            prrdz.close()


                
            #print rdz.url
            #if '.jpg' in rdz.url:
            #    img(rdz.urlz)
            #else:
            #    a(rdz.urlz)
            #h1(str(rdz.author))
            
            #li(img(i.lower(), src='%s' % i))

    with div():
        attr(cls='body')
        p('sellcoffee is open source')
        a('https://github.com/wcmckee/lcacoffee')
        #a('https://reddit.com/r/redditgetsdrawn')

print doc


# In[ ]:

docre = doc.render()
#s = docre.decode('ascii', 'ignore')
yourstring = docre.encode('ascii', 'ignore').decode('ascii')
indfil = ('/home/wcmckee/sellcoffee/index.html')
mkind = open(indfil, 'w')
mkind.write(yourstring)
mkind.close()


# In[ ]:




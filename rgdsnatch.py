# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=4>

# rgdsnatch: script to get post data from RedditGetsDrawn and post to artcontroldrawsyou

# <codecell>

import os
import random
import requests
import re
import json
import praw

# <codecell>

os.chdir('/home/pi/rgd')

# <codecell>

r = praw.Reddit(user_agent='rgdsnatch')

# <codecell>

r.login('artcontrol', 'zipit123')

# <codecell>

usrd = r.get_my_subreddits()

# <codecell>

suls = []

# <codecell>

for subs in usrd:
    print subs
    suls.append(subs)

# <codecell>

suls

# <codecell>

lesuls = len(suls)

ransuz = random.randint(0, lesuls)

thesubraz = suls[ransuz]

# <codecell>

suls

# <codecell>

print thesubraz

# <codecell>

rd = r.get_subreddit('redditgetsdrawn')

# <codecell>

rdnewz = rd.get_new()

# <codecell>

rdnew = []

# <codecell>

rdnew

# <codecell>

for uz in rdnewz:
    #print uz
    rdnew.append(uz)

# <codecell>

rdnew

# <codecell>

ransubz = random.randint(0,24)

# <codecell>

print ransubz

# <codecell>

ransev = rdnew[ransubz]

# <codecell>

rgdautoz = str(ransev.author)

# <codecell>

rgdsubred = str(ransev.subreddit)

# <codecell>

sutit = ('[' + rgdsubred + ']')

# <codecell>

sutit

# <codecell>

rgdaqwew = ('[RGD]' + rgdautoz)

# <codecell>

rgdaturo = str(ransev.url)

# <codecell>

rgdatit = str(ransev.title)

# <codecell>

rgdatit

# <codecell>

#rd.get_top

# <codecell>

linkdict = {}

# <codecell>

ophtml = open('index.html', 'w')

# <codecell>


# <codecell>

ady = r.get_subreddit('artcontroldrawsyou')

# <codecell>

comrgd =  rgdatit + ' ' + rgdaturo

# <codecell>

comrgd

# <codecell>

import time

# <codecell>

loctime = time.localtime()

# <codecell>

loctime.tm_mday

# <codecell>

loctime.tm_mon

# <codecell>

thedat = (str(loctime.tm_mday) + '/' + str(loctime.tm_mon))

# <codecell>

thedat

# <codecell>

mixtut = (thedat + sutit + rgdautoz)

# <codecell>

loctime

# <codecell>

ady.submit(mixtut , (rgdaqwew, comrgd))

# <rawcell>

# for newa in rdnew:
#     #rint newa.url
#     print len(newa)
#     htmstr = (str(newa.title) + '<a href="' + 
#                  str(newa.url) + 
#                  '"><img class="aligncenter size-large wp-image-5723" alt="' +
#                  str(newa.author) +
#                  '" src="' + 
#                  str(newa.url) + 
#                  '" /></a>')
#     #ophtml.write(htmstr)
#     #ady.submit(('[RGD]' + newa.author), newa.url)
#     print newa.author
#     #print newa.media
#     ophtml.write(htmstr)
#     print newa.selftext
#     print newa.title
#     print newa.url
#     print newa.num_comments
#     
#     linkdict.update({str(newa.author): str(newa.url)})

# <codecell>

#print str(newa.title)

# <codecell>

import json

# <codecell>

newzjson = json.dumps(linkdict)

# <codecell>

#newzjson

# <codecell>


# <codecell>

rmine = r.get_redditor('itwillbemine')

# <codecell>

#opest = open('userurl.json', 'r')
#opest.read()
#opest.close()

# <codecell>

mincom = rmine.get_comments()

# <codecell>

#print mincom

# <codecell>

minels = []

# <codecell>


dausr = {}

# <codecell>

for newa in rdnew:
    #rint newa.url
    #print newa.author
    linkdict.update({str(newa.author): str(newa.url)})

# <codecell>

for con in mincom:
    #print con.body
    minels.append(con)
    dausr.update({str(con.id): str(con.body)})

# <codecell>

minels

# <codecell>

noizjson = json.dumps(dausr)

# <codecell>

newposts = open('userurl.json', 'a')
newposts.write(newzjson)
print ('file userurl.json updated')
newcomments = open('idcomt.json', 'a')
newcomments.write(noizjson)
print ('user comments updated')
newposts.close()
newcomments.close()

# <codecell>

rdusr = str(con.author)

# <codecell>

minelsz = []

# <codecell>


# <codecell>

#for mina in minels:
    #print mina.body
   # minelsz.append(mina.body)

# <codecell>

#minelsz

# <codecell>

#mina.body

# <codecell>


# <codecell>


# <codecell>



#!/usr/bin/env python
# Get the first 20 hits for: "Breaking Code" WordPress blog
from google import search
for url in search('site:http://s2.lmcdn.fr/multimedia/', stop=5130):
     print(url)
     myfile = open("urls.txt","a")
     myfile.write(str(url)+"\n")
     myfile.close()
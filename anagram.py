#Anagram Generator
#Sathyan Sundaram (c) 2013
#Released under GPL 2.0
#
#Version 0.1

import urllib.request

word_list_link = "http://thinkpython.com/code/words.txt"

conn = urllib.request.urlopen(word_list_link)

wordlist = conn.readline()

wordlist = wordlist.strip()

wordlist = ['car','rca']
words = []
import sys
from itertools import permutations 

print("\n\nAnagram Generator\n\n")


anagram = input("What letters should be used? ")
perms = (p for p in permutations(anagram))
for p in perms:
    w = ''.join(p)
    #print(w)
    words.append(w)


words.sort()

for item in words:
    if item in wordlist:
        print(item)


#for line in wordlist:
 #   print(line)
  #  break

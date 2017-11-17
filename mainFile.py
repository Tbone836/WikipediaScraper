from bs4 import BeautifulSoup
import requests
import re
from lxml import html
import sqlite3
from patternChecker import *
from testPage import *
from nltk import *
from nltk.corpus import stopwords

#gets requests from the website
r = requests.get("https://en.wikipedia.org/wiki/Bellevue_Downtown_Park")
soup = BeautifulSoup(r.text, "lxml")

#These are the arrays storing the links
used_links = []
to_go_link = []
pattern_checker(used_links,to_go_link,soup)
stopWords = set(stopwords.words('english'))

def mainFunction():
    #The while loop will stop at 12000 to prevent computer from crashing after 12000 links

    while (len(to_go_link) < 1200):
        #For number of links in the links to go
            for link in to_go_link:
                print"hello"
                print(len(to_go_link))
                #Requesting the html from the website
                r = requests.get("https://en.wikipedia.org" + str(link))
                soup = BeautifulSoup(r.text, "lxml")
                #Uses the pattern checker to eliminate all global and image links
                pattern_checker(used_links, to_go_link, soup)
                #It then moves the link to the used list so it wont search it again.
                used_links.append(link)
                print to_go_link
                print link
                to_go_link.remove(link)
                print("used links")
                print len(used_links)
                print "to go links"
                print len(to_go_link)
                #find all of the h1 links
                '''
                findDiffTypesOfLines(soup)
                #make sure the h2 links dont have [edit] thing
                get_rid_of_edit(h2Array)
                get_rid_of_multiple_word_strings(h2Array)
                get_rid_of_multiple_word_strings_h1Array(h1Array)
                get_rid_of_multiple_word_strings_titleArray(titleArray)
                for word in h1Array:
                    if word in stopWords:
                        h1Array.remove(word)
                for word in h2Array:
                    if word in stopWords:
                        h2Array.remove(word)
                for word in titleArray:
                    if word in stopWords:
                        titleArray.remove(word)
                '''
    print h1Array
    print "DONE"
mainFunction()
'''
    while (len(to_go_link) > 0):
        for link in to_go_link:
            used_links.append(link)
            to_go_link.remove(link)
            print("used links")
            print len(used_links)
            print "to go links"
            print len(to_go_link)
            #find all of the h1 links
            findDiffTypesOfLines(soup)
            #make sure the h2 links dont have [edit] thing
            get_rid_of_edit(h2Array)
            get_rid_of_multiple_word_strings(h2Array)
            get_rid_of_multiple_word_strings_h1Array(h1Array)
            get_rid_of_multiple_word_strings_titleArray(titleArray)
            for word in h1Array:
                if word in stopWords:
                    h1Array.remove(word)
            for word in h2Array:
                if word in stopWords:
                    h2Array.remove(word)
            for word in titleArray:
                if word in stopWords:
                    titleArray.remove(word)
    print h1Array

    
mainFunction()
'''
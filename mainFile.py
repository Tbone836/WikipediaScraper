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

no_go = ["/wiki/Portal:Featured_content", "/wiki/Portal:Contents", "/wiki/Portal:Current_events",
 "/wiki/Help:Contents", "/wiki/Wikipedia:Community_portal", "/wiki/Wikipedia:About",
 "/wiki/Special:RecentChanges?hidebots=1&hidecategorization=1&hideWikibase=1&limit=50&days=7&urlversion=2",
"/wiki/Wikipedia:Contact_us", "/wiki/Special:WhatLinksHere/Wikipedia:Contact_us", "/wiki/Wikipedia:Contact_us",
"/wiki/Special:RecentChangesLinked/Wikipedia:Contact_us?hidebots=1&hidecategorization=1&hideWikibase=1&limit=50&days=7&urlversion=2",
"/wiki/Special:SpecialPages", "/wiki/Special:RecentChangesLinked/Geographic_coordinate_system"
]

#These are the arrays storing the links
used_links = []
to_go_link = []
pattern_checker(used_links,to_go_link,soup)
stopWords = set(stopwords.words('english'))

def mainFunction():
    #The while loop will stop at 12000 to prevent computer from crashing after 12000 links

    while len(to_go_link) < 400:
        #For number of links in the links to go
        for link in to_go_link:
            if len(to_go_link) < 400:
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
        print "DONE"
    for link in to_go_link:
        findDiffTypesOfLines(soup)
        #make sure the h2 links dont have [edit] thing
        get_rid_of_edit(h2Array)
        #make sure none of the strings are multiple word strings.
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
                used_links.append(link)
        #print to_go_link
        #print link
        used_links.append(link)
        to_go_link.remove(link)
        print("used links")
        print len(used_links)
        print "to go links"
        print len(to_go_link)
        print "title"
        print titleArray
        print "h1"
        print h1Array
        print "h2"
        print h2Array
        print link
mainFunction()


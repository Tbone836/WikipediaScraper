from bs4 import BeautifulSoup
import requests
import re
from lxml import html
import sqlite3
#This function checks for global or image links.
def pattern_checker(used_links, to_go_link, soup):
    #These all check for a certain pattern which we either want or don't want
    pattern = re.compile('(wiki)')
    other_language = re.compile('(https)')
    no_images = re.compile('(.jpg)')
    no_images2 = re.compile('(JPG)')
    no_same_page = re.compile('(#)')
    no_unrelatable_pages = re.compile('(//)')
    #It is going to iterate through all of the links.
    for link in soup.find_all('a'):
        #If the link is not in the used links
        if link not in used_links:
            #Getting just the href part of the <a> part of the code
            a_link = link.get('href')
            #checking to see if the pattern assigned above is in the link
            what_matches = pattern.search(str(a_link))
            international = other_language.search(str(a_link))
            get_rid_of_images = no_images.search(str(a_link))
            get_rid_of_images2 = no_images2.search(str(a_link))
            no_go_same_page = no_same_page.search(str(a_link))
            stay_relatable = no_unrelatable_pages.search(str(a_link))
            #If ==, then it is in there and we don't want it. If != then we like it.
            if what_matches != None:
                if international == None:
                    if get_rid_of_images == None:
                        if get_rid_of_images2 == None:
                            if no_go_same_page == None:
                                if stay_relatable == None:
                                    if a_link not in to_go_link:
                                        #Add the link to the togolink list.
                                        to_go_link.append(a_link)
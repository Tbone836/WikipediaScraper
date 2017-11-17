from bs4 import BeautifulSoup
import requests
import re
from lxml import html

r = requests.get("https://en.wikipedia.org/wiki/Bellevue_Downtown_Park")
soup = BeautifulSoup(r.text, "lxml")
#print(soup.prettify)
#These are all arrays that will hold an array based on type 
h1Array = []
temporaryH1Array = []

titleArray = []
temporaryTitleArray = []

h2Array = []
temporaryH2Array = []

#This will find and add all of the links of a certain type and append it to an array
def findDiffTypesOfLines(soup):
    for h1 in soup.find_all('h1'):

        h1Array.append(str(h1.text))

    for h2 in soup.find_all('h2'):

        h2Array.append(str(h2.text))

    for title in soup.find_all('title'):

        titleArray.append(str(title.text))



#If the [edit] part in in the h2, then delete it.
def get_rid_of_edit(h2Array):
    location_in_array = 0
    for item in h2Array:
        substitutionWord = re.sub('\[edit]', '', item )
        #tempSplitH2Array = item.split()
        #for value in tempSplitH2Array:
        h2Array[location_in_array] = substitutionWord
        location_in_array += 1



def get_rid_of_multiple_word_strings(h2Array):
    for item in h2Array:
        array = item.split()
        for value in array:
            temporaryH2Array.append(value)
    h2Array = temporaryH2Array

def get_rid_of_multiple_word_strings_h1Array(h1Array):
    for item in h1Array:
        array = item.split()
        for value in array:
            temporaryH1Array.append(value)
    h1Array = temporaryH1Array

def get_rid_of_multiple_word_strings_titleArray(titleArray):
    for item in titleArray:
        array = item.split()
        for value in array:
            temporaryTitleArray.append(value)
    titleArray = temporaryTitleArray

        
findDiffTypesOfLines(soup)
get_rid_of_edit(h2Array)
get_rid_of_multiple_word_strings(h2Array)
get_rid_of_multiple_word_strings_h1Array(h1Array)
get_rid_of_multiple_word_strings_titleArray(titleArray)


'''
print("This is it", splitH2Array)
getRidOfEditPattern = re.compile('\[edit]')
for word in splitH2Array:
    getRidOfEditSearch = getRidOfEditPattern.search(word)
    print getRidOfEditSearch
    if getRidOfEditSearch != None:
        for letter in word:
            wordSplitter.append(letter)
        print ("......", wordSplitter)
        wordSplitter.pop()
        wordSplitter.pop()
        wordSplitter.pop()
        wordSplitter.pop()
        wordSplitter.pop()
        wordSplitter.pop()
 
        word = ''.join(wordSplitter)
            


print splitH2Array

'''

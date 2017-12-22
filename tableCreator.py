import sqlite3

con = sqlite3.connect('webScraper.db')
cur = con.cursor()
sport1 = "soccer"
sport2 = "basketball"
sport3 = "football"
animal1 = "kangaroo"
animal2 = "dog"
KEYWORD_PARAMETER = "keyword"
LINK_PARAMETER = "link"
KEYWORD_LINKS_PARAMETER = "keyword_link"

idvariable = 1
#cur.execute("CREATE TABLE links(id INTEGER PRIMARY KEY, link TEXT)")
#con.commit()
#cur.execute("CREATE TABLE keywords(id INTEGER PRIMARY KEY, keyword TEXT)")
#con.commit()
#cur.execute("CREATE TABLE keyword_links(id INTEGER PRIMARY KEY, keyword_id INTEGER, link_id INTEGER, FOREIGN KEY(link_id) REFERENCES link(id) ON DELETE CASCADE, FOREIGN KEY(keyword_id) REFERENCES keyword(id) ON DELETE CASCADE)")
link_id = 1
keyword_id = 10

def findCount(table):
    count = cur.execute("SELECT COUNT(*) FROM ('" + table + "s')")
    rows = cur.fetchall()
    count = accessFirstValue(rows)
    return count+1


def accessFirstValue(rows):
    return rows[0][0]

def accessLinks(rows):
    return rows[0]

def insertFunction(table, item):
    countkeywords = findCount(table)
    cur.execute("INSERT INTO "+ table + "s (id," + table +") VALUES (?, ?)", (countkeywords, item.lower()))
    con.commit()
insertFunction(KEYWORD_PARAMETER, sport1)
insertFunction(KEYWORD_PARAMETER, sport2)
insertFunction(KEYWORD_PARAMETER, sport3)
insertFunction(KEYWORD_PARAMETER, animal1)
insertFunction(KEYWORD_PARAMETER, animal2)

insertFunction(LINK_PARAMETER, "wiki.com")
insertFunction(LINK_PARAMETER, "espn.com")
insertFunction(LINK_PARAMETER, "zoo.com")
insertFunction(LINK_PARAMETER, "messi.com")

countkeywords = findCount(KEYWORD_PARAMETER)
countlinks = findCount(LINK_PARAMETER)
countkeyword_links = findCount(KEYWORD_LINKS_PARAMETER)
cur.execute("INSERT INTO keyword_links(id, keyword_id, link_id) VALUES (?,?,?)", (countkeyword_links, countkeywords, countlinks))
con.commit()
def select_id_From_Table(insertion, table):
    '''
    purpose: access the id from a table of a certain link or keyword
    parameters: insertion = link or keyword we are trying to find id of, table = the table we want to use (constant)
    return: keyword_id = this is improper naming because it is supposed to represent either keyword or link id.
    '''
    #This is a quick check for what our keyword or link is
    print(insertion.lower())
    #This gets the id
    cur.execute("SELECT id FROM " + table + "s" + " WHERE "+ table + " = ('" + insertion.lower() + "')")
    #This takes all of the data it selected
    rows = cur.fetchall()
    #A check to see the format of how it is returned
    print rows
    #This finds the first value of each tuple in the returned list of tuples.
    if len(rows) == 0:
        keyword_id = accessFirstValue(rows)
        return keyword_id


def buildRelationship(keyword, link):
    countkeyword_links = findCount(KEYWORD_LINKS_PARAMETER)
    keyword_id = select_id_From_Table(keyword, KEYWORD_PARAMETER)
    link_id = select_id_From_Table(link, LINK_PARAMETER)
    cur.execute("INSERT INTO keyword_links(id, keyword_id, link_id) VALUES (?,?,?)", (countkeyword_links, keyword_id, link_id))
    print link_id


buildRelationship(sport1, "wiki.com")


def accessLinks(searched_keyword):
    cur.execute("SELECT link FROM keywords INNER JOIN keyword_links ON keywords.id = keyword_links.keyword_id INNER JOIN links ON keyword_links.link_id = links.id WHERE keyword = "+searched_keyword)
    linkrows = cur.fetchall()
    for item in linkrows:
        print item[0]

accessLinks(sport1)






#We just figured out how to make a function that associates the keyword and link on the keyword_links table.
#Figure out how to get it out of the weird return format
#Goal: Make user input keyword and then return the links that are associated with it.
#Problem: in build relationships two functions are dependent on each other running first so both are erroring out.
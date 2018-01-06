import sqlite3


con = sqlite3.connect('webScraper.db')
cur = con.cursor()
sport1 = "soccer"
sport2 = "basketball"
sport3 = "football"
animal1 = "kangaroo"
animal2 = "dog"
KEYWORD_COLUMN_PARAMETER = "keyword"
LINK_COLUMN_PARAMETER = "link"
KEYWORD_LINKS_PARAMETER = "keyword_linkS"
KEYWORDS_TABLE_PARAMETER = "keywords"
LINKS_TABLE_PARAMETER = "links"


idvariable = 1
#cur.execute("CREATE TABLE links(id INTEGER PRIMARY KEY, link TEXT)")
#con.commit()
#cur.execute("CREATE TABLE keywords(id INTEGER PRIMARY KEY, keyword TEXT)")
#con.commit()
#cur.execute("CREATE TABLE keyword_links(id INTEGER PRIMARY KEY, keyword_id INTEGER, link_id INTEGER, FOREIGN KEY(link_id) REFERENCES link(id) ON DELETE CASCADE, FOREIGN KEY(keyword_id) REFERENCES keyword(id) ON DELETE CASCADE)")
link_id = 1
keyword_id = 10

user_input = str(raw_input("What would you like to search today? Insert here: "))

def findCount(table):
    '''
    purpose: access the number of values from a table
    parameters: table(constant) that we want the count of.
    return: keyword_id = this is improper naming because it is supposed to represent either keyword or link id.
    '''
    count = cur.execute("SELECT COUNT(*) FROM ('" + table + "')")
    rows = cur.fetchall()
    count = accessFirstValue(rows)
    return count


def accessFirstValue(rows):
    return rows[0][0]

def accessLinks(rows):
    return rows[0]

def insertFunction(table, column, item):
    countkeywords = findCount(table) + 1
    cur.execute("INSERT INTO "+ table + " (id," + column +") VALUES (?, ?)", (countkeywords, item.lower()))
    con.commit()
insertFunction(KEYWORDS_TABLE_PARAMETER, KEYWORD_COLUMN_PARAMETER, sport1)
insertFunction(KEYWORDS_TABLE_PARAMETER, KEYWORD_COLUMN_PARAMETER, sport2)
insertFunction(KEYWORDS_TABLE_PARAMETER, KEYWORD_COLUMN_PARAMETER, sport3)
insertFunction(KEYWORDS_TABLE_PARAMETER, KEYWORD_COLUMN_PARAMETER, animal1)
insertFunction(KEYWORDS_TABLE_PARAMETER, KEYWORD_COLUMN_PARAMETER, animal2)

insertFunction(LINKS_TABLE_PARAMETER, LINK_COLUMN_PARAMETER, "wiki.com")
insertFunction(LINKS_TABLE_PARAMETER, LINK_COLUMN_PARAMETER, "espn.com")
insertFunction(LINKS_TABLE_PARAMETER, LINK_COLUMN_PARAMETER, "zoo.com")
insertFunction(LINKS_TABLE_PARAMETER, LINK_COLUMN_PARAMETER, "messi.com")

def select_id_From_Table(insertion, table, column):
    '''
    purpose: access the id from a table of a certain link or keyword
    parameters: insertion = link or keyword we are trying to find id of, table = the table we want to use (constant)
    return: keyword_id = this is improper naming because it is supposed to represent either keyword or link id.
    '''
    #This is a quick check for what our keyword or link is
    print(insertion.lower())
    #This gets the id
    cur.execute("SELECT id FROM " + table + " WHERE "+ column + " = ('" + insertion.lower() + "')")
    #This takes all of the data it selected
    rows = cur.fetchall()
    #A check to see the format of how it is returned
    print "rows"
    print rows
    #This finds the first value of each tuple in the returned list of tuples.
    if len(rows) != 0:
        keyword_id = accessFirstValue(rows)
        return keyword_id


def buildRelationship(keyword, link):
    countkeyword_links = findCount(KEYWORD_LINKS_PARAMETER) + 1
    keyword_id = select_id_From_Table(keyword, KEYWORDS_TABLE_PARAMETER, KEYWORD_COLUMN_PARAMETER)
    link_id = select_id_From_Table(link, LINKS_TABLE_PARAMETER, LINK_COLUMN_PARAMETER)
    cur.execute("INSERT INTO keyword_links(id, keyword_id, link_id) VALUES (?,?,?)", (countkeyword_links, keyword_id, link_id))
    con.commit()


buildRelationship(sport1, "wiki.com")
buildRelationship(sport1, "messi.com")
buildRelationship(sport1, "espn.com")
buildRelationship(sport2, "espn.com")
buildRelationship(sport2, "wiki.com")
buildRelationship(sport3, "wiki.com")
buildRelationship(sport3, "espn.com")
buildRelationship(animal1, "wiki.com")
buildRelationship(animal1, "zoo.com")
buildRelationship(animal2, "wiki.com")
buildRelationship(animal2, "zoo.com")



def accessLinks(searched_keyword):
    return_links_printed = []
    final_links_printed = []
    #cur.execute("SELECT l.* FROM keywords AS k INNER JOIN keyword_links AS kl ON k.id = kl.keyword_id INNER JOIN links AS l ON kl.link_id = l.id WHERE k.keyword = "+searched_keyword)
    #cur.execute("SELECT id FROM links WHERE link = 'wiki.com'")
    cur.execute("SELECT link_id FROM keyword_links AS kl INNER JOIN keywords AS k ON kl.keyword_id = k.id WHERE k.keyword = ?", (searched_keyword,))
    linkrows = cur.fetchall()
    print "linkrows"
    print linkrows
    for item in linkrows:
        temporary_link_id_holder = item[0]
        cur.execute("SELECT link FROM links AS l INNER JOIN keyword_links AS kl ON l.id = kl.link_id WHERE kl.link_id = ?", (str(temporary_link_id_holder)))
        rows = cur.fetchall()
        for item in rows:
            final_links_printed.append(item[0])
        final_links_printed = set(final_links_printed)
        final_links_printed = list(final_links_printed)
        print("final output!!!")
        print final_links_printed


'''
    cur.execute("SELECT link_id FROM keyword_links WHERE links.id = " + "'" + str(temporary_placeholder)+"'")
    linkrows = cur.fetchall()
    for item in linkrows:
        temporary_placeholder = item[0]
    cur.execute("SELECT keyword_id FROM keyword_links where link_id = " + "'" + str(temporary_placeholder)+"'")
    linkrows = cur.fetchall()
    for item in linkrows:
        temporary_placeholder = item[0]
    cur.execute("SELECT id FROM keywords WHERE keyword_id == " + "'" + str(temporary_placeholder)+"'")
    linkrows = cur.fetchall()
    for item in linkrows:
        temporary_placeholder = item[0]
    cur.execute("SELECT keyword FROM keywords WHERE id = " + "'" + str(temporary_placeholder)+"'")
    linkrows = cur.fetchall()
    for item in linkrows:
        temporary_placeholder = item[0]
    print temporary_placeholder
'''
accessLinks(user_input)







#We just figured out how to make a function that associates the keyword and link on the keyword_links table.
#Figure out how to get it out of the weird return format
#Goal: Make user input keyword and then return the links that are associated with it.
#Problem: in build relationships two functions are dependent on each other running first so both are erroring out.
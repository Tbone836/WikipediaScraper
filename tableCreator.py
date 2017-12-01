import sqlite3

con = sqlite3.connect('webScraper.db')
cur = con.cursor()

#cur.execute("CREATE TABLE links(id INTEGER PRIMARY KEY, link TEXT)")
#con.commit()
#cur.execute("CREATE TABLE keywords(id INTEGER PRIMARY KEY, keyword TEXT)")
#con.commit()
cur.execute("CREATE TABLE keyword_links(id INTEGER PRIMARY KEY, keyword_id INTEGER, link_id INTEGER, FOREIGN KEY(link_id) REFERENCES link(id) ON DELETE CASCADE, FOREIGN KEY(keyword_id) REFERENCES keyword(id) ON DELETE CASCADE)")

con.commit()
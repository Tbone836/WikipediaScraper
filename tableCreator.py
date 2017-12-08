import sqlite3

con = sqlite3.connect('webScraper.db')
cur = con.cursor()
sport1 = "soccer"
sport2 = "basketball"
idvariable = 1
#cur.execute("CREATE TABLE links(id INTEGER PRIMARY KEY, link TEXT)")
#con.commit()
#cur.execute("CREATE TABLE keywords(id INTEGER PRIMARY KEY, keyword TEXT)")
#con.commit()
#cur.execute("CREATE TABLE keyword_links(id INTEGER PRIMARY KEY, keyword_id INTEGER, link_id INTEGER, FOREIGN KEY(link_id) REFERENCES link(id) ON DELETE CASCADE, FOREIGN KEY(keyword_id) REFERENCES keyword(id) ON DELETE CASCADE)")
cur.execute("INSERT INTO keywords (id, keyword) VALUES (?, ?)", (idvariable, sport1))
con.commit()
idvariable += 1
cur.execute("INSERT INTO keywords (id, keyword) VALUES (?, ?)", (idvariable, sport2))
con.commit()
cur.execute("INSERT INTO links (id, link) VALUES(1, 'wiki.com')")

con.commit()
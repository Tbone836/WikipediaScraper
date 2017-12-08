import sqlite3

con = sqlite3.connect('webScraper.db')
cur = con.cursor()
cur.execute('DELETE FROM links')
con.commit()
cur.execute('DELETE FROM keywords')
con.commit()
cur.execute('DELETE FROM keyword_links')
con.commit()
import sqlite3

con = sqlite3.connect('account_logins.db')
cur = con.cursor()
cur.execute('DELETE FROM account_info')
con.commit()
from twilio.rest import Client
import sqlite3
import random

counter = 0
number = random.randint(1000, 10000)
con = sqlite3.connect('account_logins.db')
cur = con.cursor()
again = True
#cur.execute('CREATE TABLE IF NOT EXISTS account_info(id INTEGER PRIMARY KEY, username TEXT, password Text)')
#con.commit()
username = str(raw_input("Insert your username here: "))
password = str(raw_input("Insert your password here: "))
phone_number = str(raw_input("Insert your phone number here: "))
twilio_number = "+1" + str(phone_number)
cur.execute("SELECT COUNT(*) FROM account_info")
count_of_id = cur.fetchall()
for row in count_of_id:
    print(row[0])
    updating_row_id = int(row[0]) + 1


client = Client(account_sid, auth_token)

authentication_code_sent = client.messages.create(
    to=twilio_number,
    from_="+14154981248",
    body = "Your authentication code is " +str(number)
)


while again == True:
    authentication = int(raw_input("Insert the authentication code here: "))
    if authentication == number:
        cur.execute("INSERT INTO account_info (id, username, password) VALUES (?, ?, ?)", (updating_row_id, username, password))
        con.commit()
        again = False
    else:
        try_again = str(raw_input("Try Again? "))   
    if try_again.lower() == "no":
        again = False

'''
while again == True:
    authentication = int(raw_input("Insert the authentication code here: "))
    if authentication != number:
        try_again = str(raw_input("Try Again? "))
        if try_again.lower() == "no":
            again = False
            cur.execute("DELETE FROM account_info WHERE id IS?", (int(updating_row_id),))
            con.commit()
        elif try_again.lower == "yes":
            print('great!!!')
    else:
        break
        '''
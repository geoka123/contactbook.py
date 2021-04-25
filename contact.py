import sqlite3
from database import *

def run():
    print('----------------GEOKA\'S CONTACT BOOK---------------')
    print('')
    print("To see all of your contacts, press E")
    print('To add a new contact, press A')
    print('To search for a contact, press S')
    print('To update contact info, press U')
    print('To delete a contact, press D')
    print('\n')
    op1 = input('What do you want to do?  ').upper()
    if op1 == 'A':
        cname, cnumber = input('Enter a name and a number: ').split()
        cnumber = int(cnumber)
        c.execute("INSERT INTO contacts VALUES (?, ?)",(cname, cnumber))
        conn.commit()
        print('Contact added.')
    if op1 == 'E':
        c.execute("SELECT * FROM contacts")
        clist = c.fetchall()
        for item in clist:
            print('\n')
            print(item[0])
            print(item[1])
        conn.commit()
    if op1 == 'S':
        op2 = input('You wanna search by number or by contact name?    (N/C)').upper()
        if op2 == 'C':
            name1 = input('Enter contact name: ')
            c.execute("SELECT * FROM contacts")
            clist = c.fetchall()
            print('\n')
            if clist != []:
                checklst = [item for item in clist if name1 in item]
                if checklst != []:
                    for item in clist:
                        if str(name1) == item[0]:
                            print(item[0])
                            print(item[1])
                else:
                    print('This contact doesn\'t exist.')
            else:
                print('You haven\'t saved any contacts yet.')
        elif op2 == 'N':
            number = int(input('Enter contact number: '))
            c.execute("SELECT * FROM contacts")
            clist = c.fetchall()
            print('\n')
            if clist != []:
                checklst = [item for item in clist if number in item]
                if checklst != []:
                    for item in clist:
                        if int(number) == item[1]:
                            print(item[0])
                            print(item[1])
                else:
                    print('This number doesn\'t match any existing contacts.')
            else:
                print('You haven\'t saved any contacts yet.')
    if op1 == 'U':
        contactup = str(input('Which contact do yo want to update? '))
        c.execute("SELECT * FROM contacts")
        clist = c.fetchall()
        print('\n')
        if clist != []:
            checklst = [item for item in clist if contactup in item]
            if checklst != []:
                op3 = str(input('Do you want to update the contact\'s name or its number?    (C/N)')).upper()
                if op3 == 'C':
                    upname = str(input('What name do you want the contact to have? '))
                    c.execute("""UPDATE contacts SET name = (?)
                                WHERE name = (?)
        
                    """, (upname, contactup))
                    conn.commit()
                elif op3 == 'N':
                    upnum = int(input('What number do you want the contact to have? '))
                    c.execute("""UPDATE contacts SET phone = (?)
                                WHERE name = (?)
        
                    """, (upnum, contactup))
                    conn.commit()
            else:
                print('There is no such contact.')
        else:
            print('You haven\'t saved any contacts yet.')
    if op1 == 'D':
        contactdel = str(input('Which contact do yo want to delete? '))
        c.execute("SELECT * FROM contacts")
        clist = c.fetchall()
        print('\n')
        if clist != []:
            checklst = [item for item in clist if contactdel in item]
            if checklst != []:
                c.execute("""DELETE from contacts WHERE name = (?)""", (contactdel,))
                conn.commit()
                print('\n')
                print('Contact was succesfully deleted.')


run()
print('\n')
while input('Wanna use the contact book again?  (Y/N)').upper() == 'Y':
    run()

conn.close()


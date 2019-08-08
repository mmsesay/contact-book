#!/usr/bin/python

# importing mysql connector
import mysql.connector

# initiating the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root^^^",
    database="contact_book_db"
)

# cursor instance
cursor = db.cursor()

try:
    # creating the database if it doesn't exit
    cursor.execute("CREATE DATABASE IF NOT EXISTS contact_book_db")
    print('database created successfully')
except:
    print('database not found')

try:
    # creatig the database 
    cursor.execute("CREATE TABLE IF NOT EXISTS tbl_contacts (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250), address VARCHAR(250), phone VARCHAR(15), email VARCHAR(250))")
    print('table created successfully')
except:
    print('failed to create table')

# add new contact function
def addNewContact():
    ''' THIS FUNCTION REQUEST THE USER TO INPUT THE CONTACT DETAILS TO BE SAVED'''
    print('\t-------------------------------------------------')

    print('\n\t\tCREATING A NEW CONTACT')

    # request for user input
    name = input('Please enter the name: ')
    address = str(input('Please enter the address: '))
    phoneNumber = str(input('Please enter the phone number: '))
    email = input('Please enter the email: ')

    # insertion query
    query = "INSERT INTO tbl_contacts (name, address, phone, email) VALUES (%s, %s, %s, %s)"
    # storing the user inputed data to an object
    contactDetails = (name, address, phoneNumber, email) 

    # executing the query
    cursor.execute(query, contactDetails)
    db.commit() # commiting the changes

    print('***New Contact Data Saved***')
    print('\t-------------------------------------------------')

# view all contact function
def viewAllContacts():
    ''' THIS FUNCTION RETURN ALL THE SAVED CONTACT FROM THE DATABASE'''
    print('\t-------------------------------------------------')

    print('\n\t\tALL CONTACTS')
    
    # fetching query
    cursor.execute("SELECT * FROM tbl_contacts")

    # storing the result in an object
    results = cursor.fetchall()

    # looping through the result and display them
    for result in results:
        print(result)

    print('\t-------------------------------------------------')


# find a  contact function
def findAContact():
    ''' THIS FUNCTION RETURN A SPECIFIC CONTACT FROM THE DATABASE'''
    print('\t-------------------------------------------------')
    print('\n\t\tSEARCH FOR A CONTACT')
    
    # name = input('Please enter the name: ')


    print('\t-------------------------------------------------')


# user menu function
def menu():
    ''' THIS FUNCTION RETRUNS THE USER MENU '''
    print('\n\t\tWELCOME TO CONTACT BOOK CLI APP')

    # request for user input
    userMenuChoice = input(
        '''
            Reply with number 1, 2, 3 or 4:\n
            1. Add new contact\n
            2. View all contact\n
            3. Find a contact\n
            4. Exit
        ''')

    # check for user request
    if userMenuChoice == '1':
        addNewContact() # invoking the new contact funtion
        menu() # callig the function again 
    elif userMenuChoice == '2':
        viewAllContacts() # invoking the all contacts funtion
        menu() # callig the function again
    elif userMenuChoice == '3':
        findAContact() # invoking the find a contact funtion
        menu() # callig the function again
    elif userMenuChoice == '4':
        exit() # exiting the app
    else:
        print('invalid input')
        menu()
    

# # main 
if __name__=="__main__":
    menu()
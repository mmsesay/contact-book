#!/usr/bin/python

# importing mysql connector
import mysql.connector

# initiating the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root^^^",
    database="" # must enter database name here
)

# cursor instance
cursor = db.cursor()

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

    print('{} {} {} {}'.format(name, address, phoneNumber, email))
    print('data saved')
    print('\t-------------------------------------------------')

# view all contact function
def viewAllContacts():
    ''' THIS FUNCTION RETURN ALL THE SAVED CONTACT FROM THE DATABASE'''
    print('\t-------------------------------------------------')

    print('\n\t\tALL CONTACTS')
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
    print('\n\t\tWELCOME TO CONTACT BOOK')

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
    


# main 
if __name__=="__main__":
    menu()
import csv
import os
#this module makes it easy to convert the dates into ISO format, which I can do operations against
#pip install python-dateutil
from dateutil.parser import parse




# Getting List of all files
from csv import DictReader


def get_files():
    f = []
    # here we get all files that end with csvs and append to list
    for (root, dirs, files) in os.walk('.'):
        for filename in files:
            if filename.endswith('.csv'):
                f.append(filename)

    user_input = True
    # Ask user for input and set filename based on that
    print('*' * 80)
    print('Found the following Files!')
    print('*' * 80)

    # enumerate the list
    for num, file in enumerate(f, 1):
        print('{} - {}'.format(num, file))

    print('*' * 80)
    file_choice = input('Select a file by Number\n')

    # I was going to do some checking; but am 2 dumb 2 figure out
    # so just converting to int and passing that to list
    # subtracting one, becuase lists start at 0
    file_choice = int(file_choice) - 1
    file_choice = f[file_choice]

    print('*' * 80)
    print('Opening the following File!\n{}'.format(file_choice))
    print('*' * 80)

    # return the variable so it can be used outside of the function
    return file_choice


# actually working with the file here

# get_files()

# calling function and saving the returned value file_choice to a new variable
selected_file = get_files()

    #Asks user for date
start_date = input('Enter Start Date (M/D/YYYY)\n')
start_date = parse(start_date)




###################################################
#INITIALZING DICT WITH KEYS, TO CALL FOR HEADERS!
###################################################
contact = {
    'First Name': '',
    'Last Name': '',
    'Gender': '',
    'Date of Birth': '',
    'Childs Age': '',
    'Authorized Pick up #1': '',
    'Authorized Pick up #2': '',
    'Authorized Pick up #3': '',
    'Emergency Contact Name': '',
    'Emergency Contact Phone': '',
    'Parent #1': '',
    'Parent #2': '',
    'Primary Phone Parent #1': '',
    'Primary Phone Parent #2': '',
    'Registration Date': ''
    }

red_flags = {
    'First Name': '',
    'Last Name' : '',
    'Gender' : '',
    'Child\'s Age': '',
    'Child\'s Grade' : '',
    'Does your child have any special needs we need to be aware of?' :''
    }

rides = {
    'First Name': '',
    'Last Name' : '',
    'Gender' : '',
    'Child\'s Age': '',
    'Child\'s Grade' : '',
    'Child\'s Shcool' : '',
    'Days Attending': '',
    'Code Word - Used at time of pick up each day': ''
    }


######################################################
#READING FIRST FILE, AND CREATING CONTACT SHEET
######################################################

with open(selected_file, 'r') as csv_reader:
    with open ( 'contact_sheet.csv' , 'w+' ) as contact_sheet:
        csv_data = csv.DictReader(csv_reader)

        #write header based on keys for contact sheet
        #This is nested under the with open for contact sheet
        contact_data = csv.DictWriter ( contact_sheet , contact.keys () )
        contact_data.writeheader()

        for data in csv_data:
            reg_time = parse(data['Registration Date'])




            if reg_time >= start_date:

                contact.update ({
                    'First Name' : data.get ( 'First Name' , '' ) ,
                    'Last Name' : data.get ( 'Last Name' , '' ) ,
                    'Gender' : data.get ( 'Gender' , '' ) ,
                    'Date of Birth' : data.get ( 'Date of Birth' , '' ) ,
                    'Childs Age' : data.get ( 'Child\'s Age' , '' ) ,
                    'Authorized Pick up #1' : data.get ( 'Authorized Pick Up #1' , '' ) ,
                    'Authorized Pick up #2' : data.get ( 'Authorized Pick Up #2' , '' ) ,
                    'Authorized Pick up #3' : data.get ( 'Authorized Pick Up #2' , '' ) ,
                    'Emergency Contact Name' : data.get ( 'Emergency Contact Name' , '' ) ,
                    'Emergency Contact Phone' : data.get ( 'Emergency Contact Phone' , '' ) ,
                    'Parent #1' : data.get ( 'Parent #1' , '' ) ,
                    'Parent #2' : data.get ( 'Parent #2' , '' ) ,
                    'Primary Phone Parent #1' : data.get ( 'Primary Phone Parent #1' , '' ) ,
                    'Primary Phone Parent #2' : data.get ( 'Primary Phone Parent #2' , '' ),
                    'Registration Date': data.get('Registration Date', '')

                } )
                contact_data.writerow(contact)
            elif reg_time < start_date:
                continue

    contact_sheet.close()
    csv_reader.close

#################################################################
#Here we Work with the RED FLAGS CSV
##################################################################
with open ( selected_file , 'r' ) as csv_reader :
    with open('red_flags.csv', 'w+') as red_flags_sheet:
        csv_data = csv.DictReader ( csv_reader )

        red_flags_data = csv.DictWriter(red_flags_sheet, red_flags.keys())
        red_flags_data.writeheader()

        #looping through data in first read file

        for flags in csv_data:
            reg_time = parse(flags['Registration Date'] )


            if reg_time >= start_date :
                red_flags.update({
                    'First Name' : flags.get('First Name', '') ,
                    'Last Name' : flags.get('Last Name', '') ,
                    'Gender' : flags.get('Gender', '') ,
                    'Child\'s Age' : flags.get('Child\'s Age', '') ,
                    'Child\'s Grade' : flags.get('Child\'s Grade', '') ,
                    'Does your child have any special needs we need to be aware of?' : flags.get('Does your child have any special needs we need to be aware of?', '')
                })
                red_flags_data.writerow(red_flags)
            elif reg_time > start_date:
                continue
    red_flags_sheet.close()
    csv_reader.close()

#############################################
#here we create the RIDES CSV
#############################################
with open ( selected_file , 'r' ) as csv_reader :
    with open('rides_sheet.csv', 'w+') as rides_sheet:
        csv_data = csv.DictReader ( csv_reader )

        rides_data = csv.DictWriter(rides_sheet, rides.keys())
        rides_data.writeheader()

        for items in csv_data:
            reg_time = parse ( items['Registration Date'] )

            if reg_time >= start_date :
                rides.update({
                    'First Name': items.get('First Name', '') ,
                    'Last Name': items.get('Last Name', '') ,
                    'Gender': items.get('Gender', '') ,
                    'Child\'s Age': items.get('Child\'s Age', '') ,
                    'Child\'s Grade': items.get('Child\'s Grade', '') ,
                    'Child\'s Shcool':  items.get('Child\'s School', ''),
                    'Days Attending': items.get('Days Attending', '') ,
                    'Code Word - Used at time of pick up each day': items.get('Code Word - Used at time of pick up each day', '')
                })
                rides_data.writerow(rides)
            elif reg_time > start_date:
                continue
    rides_sheet.close()
    csv_reader.close()

print('*' * 80)
print('Process Finished!')
print('*' * 80)

















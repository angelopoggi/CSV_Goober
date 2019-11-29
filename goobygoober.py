########################
# Y M C A GOOBY GOOBER
# BY: ANGELO POGGI
# apoggi226@gmail.com
#
#########################

import csv
import pandas as pd
import os
import pprint



# Getting List of all files
def get_files():
    f = []
    # here we get all files that end with xlsx and append to list
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

#opening the CSV file and writing changes to new file

#Open the Exsisting the File



with open(selected_file, 'r') as csv_reader:
    with open('contact_sheet.csv', 'a') as contact_sheet:
        line = csv_reader.readline()
        cnt = 1
        while line:
            print(line)
            if cnt == 1:
                header_names = [
                    'First Name' , #2
                    'Last Name' , #3
                    'Gender' , #4
                    'Date of Birth' #5,
                    'Childs Age' , #22
                    'Authorized Pickup #1' , #55
                    'Authorized Pickup #2' , #56
                    'Authorized Pickup #3' , #57
                    'Emergency Contact Name' , #43
                    'Emergency Contact Phone' , #43
                    'Parent #1' ,#49
                    'Prent #2' ,#52
                    'Primary Phone Parent #1' , #50
                    'Primary Phone Parent #2' #53
                ]
                #
                contact_sheet.write(','.join(header_names))
            else:
                line_list = line.split(',')
                #FIX THIS
                final_row = "{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(line_list[2],line_list[3],
                                                                               line_list[4],line_list[5],
                                                                               line_list[22],line_list[55],
                                                                               line_list[56],line_list[57],
                                                                               line_list[43],line_list[44],
                                                                               line_list[49],line_list[52],
                                                                               line_list[50],line_list[53])
                print(final_row)
                contact_sheet.write('\n')
                contact_sheet.write(final_row)
            line = csv_reader.readline()
            cnt += 1

    #csv_reader = csv.reader(csv_reader)


    # '''
    # 1 - Recereate the header as List; but write that as a row
    # 2 - then take list then do .join and pass it a commma
    # 3 - pass writerow the header_name.join(')
    # '''




#contact = {}

    # #with open ( 'contact_sheet.csv' , 'a' ) as contact_sheet :
    #     print(csv_reader.readline())
    #     test = csv.DictWriter(contact_sheet, csv_reader.readline().split(','))
    #     #test.writerow(','.join(header_names))'''















        for data in csv_reader:

            contact.update({
                'First Name': data.get('First Name', ''),
                'Last Name': data.get('Last Name', ''),
                'Gender': data.get('Gender', ''),
                'Date of Birth': data.get('Date of Birth', ''),
                'Childs Age': data.get('Child\'s Age', ''),
                'Authorized Pick up #1': data.get('Authorized Pick Up #1', ''),
                'Authorized Pick up #2': data.get('Authorized Pick Up #2', ''),
                'Authorized Pick up #3': data.get('Authorized Pick Up #2', ''),
                'Emergency Contact Name': data.get('Emergency Contact Name', ''),
                'Emergency Contact Phone': data.get('Emergency Contact Phone', ''),
                'Parent #1': data.get('Parent #1', ''),
                'Parent #2' : data.get('Parent #2', ''),
                'Primary Phone Parent #1': data.get('Primary Phone Parent #1', ''),
                'Primary Phone Parent #2': data.get('Primary Phone Parent #2', '')

            })



            #test.writerow(contact)








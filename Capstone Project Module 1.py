# Main Data
import pandas as pd
import re
ExistingData = {'No' : ['1','2','3','4','5'],
                'Business ID' : ['RI12','YF31','TS11','JC31','KC22'],
                'Business Name' : ['Royal Inn','Yin Fang','The Smiths','Johns Co','Kuro Coffee'],
                'Business Type' : ['Hotel','Food & Beverages','Supermarket','Property','Food & Beverages'],
                'Website' : ['royalinn.com','yinfanrestaurant.com','thesmiths.com','johnscoproperty.com','kurocoffee.com'],
                'Email' : ['royalinn@gmail.com','yinfang@gmail.com','thesmiths@yahoo.com','johnsco@gmail.com','kurocoffee@gmail.com'],
                'Address' : ['3 Burnswick Mews','4 Collingham PLace','12 Westway road','9 Oxford Street','10 Thames Way'],
                'Postcode' : ['SW2 9IL','S12 8UL','W11 1OP','E98 8IK','NW1 3HM'],
                'City' : ['London','London','Birmingham','Manchester','York'],
                'Country' : ['United Kingdom','United Kingdom','United Kingdom','United Kingdom','United Kingdom'],
                'Country Code' : ['+44', '+44', '+44', '+44', '+44'],
                'Phone' : ['76231233','09123838','12398883','712999823','78465923']}

TableExistingData = pd.DataFrame(ExistingData)
MainExistingData = TableExistingData.set_index('No', drop=True)

def DataKeys():
    keys = MainExistingData.columns
    output_string = ""
    for i, j in enumerate(keys, start=1):
        output_string += f'{i}. {j}\n'
    return output_string

# Main Menu
def MainMenu():
    while (True):
        print('\n=================== Main Menu ===================')
        print('''
1: Display or Search Yellow Pages (Phone Book Data)
2: Add data to the Yellow Pages
3: Update Yellow Pages Data
4: Delete Yellow Pages Data
5: Exit
''')

        MenuInput = input('Please enter your selection (1-5): ')
        if MenuInput == '1':
            DisplayData()
        elif MenuInput == '2':
            AddData()
        elif MenuInput == '3':
            UpdateData()
        elif MenuInput == '4':
            DeleteData()
        elif MenuInput == '5':
            print('Thank you and Good Bye!')
            break
        else:
            WrongInput()

# Read Menu
def DisplayData():
    while True:
        print('\n=================== Display Data Menu ===================')
        print('''
1. Display all data
2. Search specific data
3. Back to Main Menu
''')
        DisplayDataMenuInput = input('Please enter your selection (1-3): ')
        if DisplayDataMenuInput == '1':
            DisplayAllData()
        elif DisplayDataMenuInput == '2':
            DisplaySpecificData()
        elif DisplayDataMenuInput == '3':
            break
        else:
            WrongInput()
    
def DisplayAllData():
    print('\n=================== Yellow Pages (Phone Book Database) ===================')   
    if MainExistingData is not None:
        print(MainExistingData)
    else:
        print('The Data does not exist')

def DisplaySpecificData():
    if MainExistingData is not None:
        while True:
            print('\n=================== Display Specific Data Menu ===================')
            print('''
1. Search based on Categories
2. Back to Display Data Menu
3. Back to Main Menu
''')
            SearchInput = input('Please enter your selection (1-3): ')
            if SearchInput == '1':
                while True: 
                    try:
                        print('\n=================== Categories From Phonebook Database ===================')
                        print('Select one of the following numbers: ')
                        print(DataKeys(), end='')
                        print('12. Go back to Display Specific Data Menu')
                        global number
                        number = int(input('\nPlease choose the number of categories you wish to look up into: '))
                        if 1 <= number <= len(MainExistingData.columns):
                            SelectColumn()
                        elif number == int(12):
                            break
                        else:
                            WrongInput()
                    except ValueError:
                        print('\nPlease input number (integer) as your selection')
            elif SearchInput == '2':
                break
            elif SearchInput == '3':
                MainMenu()
                break
            else:
                WrongInput()
    else:
        print('The Data does not exist')

def SelectColumn():
    while True:
        try:
            selected_column = list(MainExistingData.columns)[number - 1]
            selected_rows = MainExistingData[selected_column]
            print(f'''
\nHere are category {selected_column} data from the phone book database: 
{selected_rows}
''', end='')
            print('12. Go back to Category Search')
            print('cancel. Go back to Main Menu')
            global searchdata
            searchdata = int(input('Please select one of the data from category (input numbers): '))
            if 1 <= searchdata <= len(selected_rows):
                SelectRowFromColumn()
            elif searchdata == int(12):
                break
            elif searchdata == 'cancel':
                MainMenu()
            else:
                WrongInput()
        except ValueError:
            print('Please input number (integer) as your selection')

def SelectRowFromColumn():
    while True:
        try:
            selected_row = MainExistingData.iloc[searchdata - 1]
            print('Here is the data that you are looking for: ')
            max_key_length = max(len(str(col)) for col in selected_row.index)
            for col, value in selected_row.items():
                print(f'{col:{max_key_length}}: {value}')
            print('''\n
0. Go back to data selection from category
1. Go back to Main Menu
                  ''')
            inputan = input('Please enter your selection (0-1): ')
            if inputan == '0':
                break
            elif inputan == '1':
                MainMenu()
            else:
                WrongInput()
        except ValueError:
            print('Please input number (integer) as your selection')

# Create menu
def AddData():
    while True:
        print('\n=================== Add Data Menu ===================')
        print('''
1. Add new data to Phone Book Database
2. Back to Main Menu''')
        inputannya = input('Please enter your selection (1-2): ')
        if inputannya == '1':
            InputNewData()
        elif inputannya == '2':
            break
        else:
            WrongInput()

newinput_dict = {}
def InputNewData():
    global MainExistingData
    while True:
        print('Here are the available phonebook database: ')
        print(MainExistingData)
        
          # Flag variable to track if the user wants to continue adding data
        while True:
            exit_input = input('Enter "cancel" to go back or press Enter to continue add data: ')
            if exit_input.lower() == 'cancel':
                # User canceled, exit the input function and return to the menu
                return
            elif exit_input.strip() == '':
                print("Please enter the data: ")
            else:
                WrongInput()
            Input_Conditions()
            MainExistingData = CreateNewData(MainExistingData, newinput_dict)
            MainExistingData.index = [''] * len(MainExistingData)

            exit_input = input('Enter "done" to finish or press Enter to see added data and continue to add data: ')
            if exit_input.lower() == 'done':
                break
            print(MainExistingData)

def CreateNewData(df, new_data):
    new_df = pd.DataFrame([new_data])
    df = pd.concat([df, new_df], ignore_index=True)
    df['No'] = df.index + 1  # Set 'No' column to index + 1
    # Move 'No' column to the most left
    cols = ['No'] + [col for col in df if col != 'No']
    df = df[cols]
    df.reset_index(drop=True, inplace=True)  # Reset the index and drop the old index
    return df

def Input_Conditions():
    while True:
        while True:
            businessidinput = input('Enter Business ID: ').upper()
            patternbusinessid = r'^[A-Z]{2}\d{2}$'
            if re.match(patternbusinessid, businessidinput):
                newinput_dict['Business ID'] = businessidinput
                break
            else:
                WrongInput()

        businessnameinput = input('Enter Business Name: ')
        businesstypeinput = input('Enter Business Type: ')
        if not (isinstance(businessnameinput, str) and isinstance(businesstypeinput, str)):
            WrongInput()
            continue
        newinput_dict['Business Name'] = businessnameinput
        newinput_dict['Business Type'] = businesstypeinput

        while True:
            websiteinput = input('Enter Website (format: http://, https://): ')
            patternwebsiteinput = r'https?://\S+'
            if re.match(patternwebsiteinput, websiteinput):
                newinput_dict['Website'] = websiteinput
                break
            else:
                WrongInput()

        while True:
            emailinput = input('Enter Email: ')
            patternemailinput = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if re.match(patternemailinput, emailinput):
                newinput_dict['Email'] = emailinput
                break
            else:
                WrongInput()

        addressinput = input('Enter Address: ')
        if not (isinstance(addressinput, str)):
            WrongInput()
            continue
        newinput_dict['Address'] = addressinput    

        while True:
            postcodeinput = input('Enter PostCode: ').upper()
            patternpostcode = r'^[A-Z0-9]{5,}$'
            if re.match(patternpostcode, postcodeinput):
                newinput_dict['Postcode'] = postcodeinput
                break
            else:
                WrongInput()

        while True:
            cityinput = input('Enter City: ')
            countryinput = input('Enter Country: ')
            if isinstance(cityinput, str) and isinstance(countryinput, str):
                newinput_dict['City'] = cityinput
                newinput_dict['Country'] = countryinput
                break 
            else:
                WrongInput()

        while True:
            countrycode = input('Enter CountryCode (format: +2digits): ')
            patterncountrycode = r'^\+\d{2}$'
            if re.match(patterncountrycode,countrycode):
                newinput_dict['Country Code'] = countrycode
                break
            else:
                WrongInput()

        while True:
            phone = input('Enter Phone Number: ')
            if phone.isnumeric() and 6 <= len(phone) <= 12:
                newinput_dict['Phone'] = phone
                break
            else:
                WrongInput()
        break
#Update Menu
def UpdateData():
    while True:
        print('\n=================== Update Data Menu ===================')
        print('''
1. Update data from Phone Book Database
2. Back to Main Menu
              ''')
        User_Input = input('Please enter your selection (1-2): ')
        if User_Input == '1':
            Display_row_to_Update_Phonebook_Data(MainExistingData)
        elif User_Input == '2':
            break
        else:
            WrongInput()

def Display_row_to_Update_Phonebook_Data(df):
    print(df)
    print('''
Please choose one of the following:
1. Choose which data to change from phonebook database
2. Back to Update Data Menu
              ''')
    while True:    
        ChooseOption = input('Please enter your selection (1-2): ')
        if ChooseOption == '1':
            indexNo = int(input('Please choose which rows to update: '))
            index = indexNo - 1
            if 0 <= index < len(df):
                selected_row = pd.DataFrame(df.iloc[index]).transpose()
                print(selected_row)
                newinput_dict = Input_for_Update_Data(selected_row, index)
                df = Updating_Data(df, index, newinput_dict)
            else:
                print('The data you are looking for does not exist')
        elif ChooseOption == '2':
            break
        else:
            WrongInput()    

def Updating_Data(df, index, newinput_dict):
    if 0 <= index < len(df):
           for col, value in newinput_dict.items():
            df.loc[df.index[index], col] = value
    else:
        print('The data you are looking for does not exist')
    
    return df

def Input_for_Update_Data(df, index):
    newinput_dict = {}
    
    patternbusinessid = r'^[A-Z]{2}\d{2}$'
    patternwebsiteinput = r'https?://\S+'
    patternemailinput = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    patternpostcode = r'^[A-Z0-9]{5,}$'
    patterncountrycode = r'^\+\d{2}$'
    
    while True:
        column_to_update = input("Enter the column you want to update (or 'done' to finish): ")
        if column_to_update.lower() == 'done':
            print('''
Please choose one of the following:
1. Choose which data to change from phonebook database
2. Back to Update Data Menu
              ''')
            break

        if column_to_update in df.columns:
            if column_to_update == 'Business ID':
                new_value = input(f"Enter the new value for '{column_to_update}' (format: XX99): ").upper()
                if re.match(patternbusinessid, new_value):
                    newinput_dict[column_to_update] = new_value
                    print(f'You have successfully added {new_value} to {column_to_update} column')
                else:
                    print(f"Invalid input for '{column_to_update}'")
            elif column_to_update == 'Website':
                new_value = input(f"Enter the new value for '{column_to_update}' (format: http:// or https://): ")
                if re.match(patternwebsiteinput, new_value):
                    newinput_dict[column_to_update] = new_value
                    print(f'You have successfully added {new_value} to {column_to_update} column')
                else:
                    print(f"Invalid input for '{column_to_update}'")
            elif column_to_update == 'Email':
                new_value = input(f"Enter the new value for '{column_to_update}': ")
                if re.match(patternemailinput, new_value):
                    newinput_dict[column_to_update] = new_value
                    print(f'You have successfully added {new_value} to {column_to_update} column')
                else:
                    print(f"Invalid input for '{column_to_update}'")
            elif column_to_update == 'Postcode':
                new_value = input(f"Enter the new value for '{column_to_update}': ")
                if re.match(patternpostcode, new_value):
                    newinput_dict[column_to_update] = new_value
                    print(f'You have successfully added {new_value} to {column_to_update} column')
                else:
                    print(f"Invalid input for '{column_to_update}'")
            elif column_to_update == 'Country Code':
                new_value = input(f"Enter the new value for '{column_to_update}' (format: +2digits): ")
                if re.match(patterncountrycode, new_value):
                    newinput_dict[column_to_update] = new_value
                    print(f'You have successfully added {new_value} to {column_to_update} column')
                else:
                    print(f"Invalid input for '{column_to_update}'")
            else:
                new_value = input(f"Enter the new value for '{column_to_update}': ")
                print(f'You have successfully added {new_value} to {column_to_update} column')
                newinput_dict[column_to_update] = new_value
        else:
            print(f"'{column_to_update}' is not a valid column in the DataFrame.")
    
    return newinput_dict

# Delete menu
def DeleteData():
    while True:
        print('============= Delete Data Menu =============')
        print('''
1. Delete data from Phone Book Database
2. Access Recycle Bin
3. Back to Main Menu
''')
        input_delete = input('Please enter your selection (1-2): ')
        if input_delete == '1':
            Delete_Specific_Data_Row(MainExistingData)
        elif input_delete == '2':
            Recycle_Bin_Access()
        elif input_delete == '3':
            MainMenu()
        else:
            WrongInput()

def Delete_Specific_Data_Row(df):
    while True:
        print(MainExistingData)
        global input_row_delete
        input_row_delete = input('Please input which row to delete: ')
        input_row_delete_condition = int(input_row_delete)
        if 1 <= input_row_delete_condition <= len(df):
            Data_Deletion_Option(df, input_row_delete)
        else:
            print('The data you are looking for does not exist')
            break

def Data_Deletion_Option(df, index):
    while True:
        Recycle_Bin_Data = df.loc[index]
        print(pd.DataFrame(Recycle_Bin_Data).transpose())
        deleteconfirmation = input('Are you sure you want to delete this row? (Y/N)').upper()
        if deleteconfirmation == 'Y':
            df.drop(index, axis=0, inplace=True)
            Recycle_Bin(Recycle_Bin_Data)
            print(df)
            DeleteData()
        elif deleteconfirmation == 'N':
            break
        else:
            WrongInput()

Recycle = pd.DataFrame()
def Recycle_Bin(data):
    global Recycle
    Recycle = Recycle.append(data, ignore_index=True)
    Recycle.reset_index(drop=True, inplace=True)
    Recycle.index += 1
    Recycle.index.name = 'No'
    print('Deleted data is now in Recycle Bin')
    
def Recycle_Bin_Access():
    global Recycle, MainExistingData
    while True:
        print(Recycle)
        print('''
1. Empty Recycle Bin
2. Restore Recycle Bin
3. Back to Main Menu
''')
        inputrecycle = input('Enter your selection (1-2): ')
        if inputrecycle == '1':
            Recycle = pd.DataFrame(columns=Recycle.columns)
            print('Recycle Bin is now empty')
        elif inputrecycle == '2':
            MainExistingData = pd.concat([MainExistingData, Recycle])
            break
        elif inputrecycle == '3':
            MainMenu()
        else:
            WrongInput()

# Wrong Input
def WrongInput():
    print('Error: your input format is wrong') 

MainMenu()
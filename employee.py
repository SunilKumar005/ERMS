import sqlite3
from constant import *
import os
import sys
import base64
import datetime
import random
import pytz
from os import *
from tabulate import tabulate
from colorama import Fore
from subprocess import call


class DatabaseWrapper:

    def __init__(self, db_name):
        self.db_name = db_name

    def db_query(self, cmd, args=[]):
        database = sqlite3.connect(self.db_name)
        sql = database.cursor().execute(cmd, args)
        global data
        data = sql.fetchall()
        database.close()

    def db_query1(self, cmd, args=[], fetchone=True):
        database = sqlite3.connect(self.db_name)
        sql = database.cursor().execute(cmd, args)
        global data1
        data1 = sql.fetchone()[0] 
        database.close()
        

    def db_execute(self, cmd, args=[]):
        database = sqlite3.connect(self.db_name)
        database.cursor().execute(cmd, args)
        database.commit()
        database.close()

class Records(DatabaseWrapper):

    def __init__(self):
        super().__init__(db_path)

    def create_table(self):
        self.db_execute('''
        CREATE TABLE IF NOT EXISTS
        Records(
            employee_id TEXT NOT NULL,
            employee_name TEXT NOT NULL,
            age INTEGER NOT NULL,
            salary INTEGER NOT NULL,
            increment INTEGER NOT NULL,
            experience_in_years INTEGER NOT NULL,
            email_id TEXT,
            mobile_no INTEGER NOT NULL,

            UNIQUE(employee_id)
            UNIQUE(email_id)
            UNIQUE(mobile_no)
        );''')
        self.db_execute('''
        CREATE TABLE IF NOT EXISTS
        Changes(
            Changes_id TEXT NOT NULL,
            Description TEXT NOT NULL,
            Date TEXT NOT NULL,
            Time TEXT NOT NULL,

            UNIQUE(Changes_id)
        );''')
        self.db_execute('''
        CREATE TABLE IF NOT EXISTS
        Address(
            employee_id TEXT NOT NULL,
            employee_name TEXT NOT NULL,
            address TEXT NOT NULL,
            state TEXT NOT NULL,

            UNIQUE(employee_id)
        );''')

    def rerun_program(self):
        rerun_option = input(Fore.YELLOW + "\nDo you want to Rerun the program [y/n]: " + Fore.RESET)
        if rerun_option == 'y':
            os.execv(sys.executable, ['python3'] + [sys.argv[0]])
        else:
            return

    def add_changes(self, description):
        present_date = datetime.date.today().strftime("%B %d, %Y")
        present_time_zone = pytz.timezone('Asia/Kolkata')
        present_time = datetime.datetime.now(present_time_zone).strftime("%I:%M:%S %p")
        alphabets1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        numbers1 = ['1','2','3','4','5','6','7','8','9','0']
        numbers2 = ['1','2','3','4','5','6','7','8','9','0']
        alphabets2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        fingerprint = random.choice(alphabets1) + random.choice(numbers1) + random.choice(numbers2) + random.choice(alphabets2)
        if description == False:
            return 
        self.db_execute('''
        INSERT INTO Changes(Changes_id, Description, Date, Time)
        VALUES(?, ?, ?, ?);''', args=[fingerprint, description , present_date , present_time])
        

    def check_table_exists(self):
        try:
            self.db_query('SELECT * FROM Records;')
        except :
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + ']' +Fore.YELLOW + " Table Doesn't Exist or been Deleted !!! [Maybe You have not created it yet]" + Fore.RESET)
            exit()

    def check_table_exists1(self):
        try:
            self.db_query('SELECT * FROM Records;')
        except:
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + ']' +Fore.YELLOW + " Table has Already been Deleted and All data in them too !!! [Maybe You have not created it yet] " + Fore.RESET)
            exit()
 
    def view_secret_table(self):
        self.db_query('SELECT * FROM Changes;')
        print(Fore.YELLOW + '\nChanges Applied :\n' + Fore.RESET)
        print(tabulate(data, headers=['Changes Id', ' Description about the Changes Made ', 'Date', 'Time'], tablefmt='psql')) 

    def assign_description(self, choice):
        global description2
        description2 = "Program was ran and number " + choice + " was chosen"
        if len(choice) == 0:
            description2 = 'Program was ran and User Exited the program'
        elif type(choice) == str:
            if choice == 'thisisunstoppable':            
                description2 = 'Program was ran and Secret Changes Table option was chosen'
            elif int(choice) < 11:
                description2 = "Program was ran and number " + choice + " was chosen"
            else:
                description2 = 'Program was ran and Invalid number or string was chosen'   
            
        
    def add_employee_address(self , employee_id , employee_name , address , state):
        self.db_execute('''
        INSERT INTO Address(employee_id ,employee_name ,address ,state)
        VALUES(?, ?, ?, ?);''', args=[employee_id, employee_name, address, state])        

    def add_employee(self ,employee_id ,employee_name ,age ,salary ,increment ,experience_in_years ,email_id ,mobile_no):
        self.db_execute('''
        INSERT INTO Records(employee_id ,employee_name ,age ,salary ,increment ,experience_in_years ,email_id ,mobile_no)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?);''', args=[employee_id, employee_name, age, salary, increment, experience_in_years, email_id, mobile_no])

    def check_add_employee_value(self, value):
        if len(value) == 0:
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + ']' +Fore.YELLOW + " Please Enter any Valid Value !!! " + Fore.RESET)
            exit()

    def clear_data(self):
        permission_for_clear = input(Fore.YELLOW + "\nAll the Records will be destroyed, Are you sure you want to Continue?[y/n]: " + Fore.RESET)
        if permission_for_clear == 'y':
            self.db_execute('''
            DELETE FROM Records;''')
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + ']' +Fore.YELLOW + " Successfully Deleted all Records !!! " + Fore.RESET)
        else:
            print(Fore.YELLOW + '\nAborted !' + Fore.RESET)
            return

    def delete_table(self):
        permission_for_delete = input(Fore.YELLOW + "\nThe Table will be deleted and You'll need to create It again, Are you sure want to Continue?[y/n]: " + Fore.RESET)
        if permission_for_delete == 'y':
            self.db_execute("DROP TABLE Records;")
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + ']' +Fore.YELLOW + " Successfully Deleted the Table !!!" + Fore.RESET)
            global description1
            description1 = "Table Records and All the data in it was Deleted"
        else:
            print('\nAborted !')
            description = False

    def clear_employee_data(self, employee_id):
        self.db_execute('''
        DELETE FROM Records
        WHERE employee_id=?;''', args=[employee_id])
        self.db_execute('''
        DELETE FROM Address
        WHERE employee_id=?;''', args=[employee_id])
        print('\n[' + Fore.YELLOW + '!' + Fore.RESET + ']' +Fore.YELLOW + " Successfully Delected the Choosen Records !!!" + Fore.RESET)

    def view_all_data(self):
        self.db_query('SELECT * FROM Records;')
        print(tabulate(data, headers=['Employee Id', 'Employee Name', 'Age', 'Salary', 'Increment (per Year)','Experience' , 'Email Id (Not Compulsary)', 'Mobile No.'], tablefmt='psql'))
        return

    def view_address_data(self):
        self.db_query('SELECT * FROM Address;')
        print(tabulate(data, headers=['Employee Id', 'Employee Name', 'Address' ,'State & Country'], tablefmt='psql'))
        return


    def update_data_id(self, employee_id, employee_name, age, salary, increment, experience_in_years, email_id, mobile_no, address, state):
        self.db_execute('''
        UPDATE Records
        SET employee_name=?, age=?, salary=?, increment=?, experience_in_years=?, email_id=?, mobile_no=?
        WHERE employee_id=?;''', args=[employee_name, age, salary, increment, experience_in_years, email_id, mobile_no, employee_id])
        self.db_execute('''
        UPDATE Address
        SET employee_id=?, employee_name=?, address=?, state=?
        WHERE employee_id=?;''', [employee_id, employee_name, address, state, employee_id])

    
    def update_data_name(self, employee_id, employee_name, age, salary, increment, experience_in_years, email_id, mobile_no, address, state):
        self.db_execute('''
        UPDATE Records
        SET employee_id=?, age=?, salary=?, increment=?, experience_in_years=?, email_id=?, mobile_no=?
        WHERE employee_name=?;''', args=[employee_id, age, salary, increment, experience_in_years, email_id, mobile_no, employee_name])
        self.db_execute('''
        UPDATE Address
        SET employee_id=?, employee_name=?, address=?, state=?
        WHERE employee_name=?;''', [employee_id, employee_name, address, state, employee_name])

   
    def clear_screen(self): 
        _ = call('clear' if os.name =='posix' else 'cls') 
 
    def magic_word_authentication(self):
        print(Fore.YELLOW + "\nAuthentication is required to perform this kind of Operations !!!")
        magic_word_check = input(Fore.YELLOW + '\nPlease Enter the Password to Continue : ' + Fore.RESET)
        magic_word2 = base64.b85decode(magic_word)
        magic_word3 = magic_word2.decode('UTF-8')
        if magic_word_check == magic_word3:
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + ']' + Fore.YELLOW + ' Authentication Successful !!! ' + Fore.RESET)
        else:
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + ']' + Fore.YELLOW + " Password Incorrect !!! [You don't own the right to delete]")
            exit()

    def default_name(self, employee_id):
        self.db_query1('SELECT employee_name FROM Records WHERE employee_id=?;', [employee_id])
        global default_employee_name
        default_employee_name = data1

    def default_age(self, employee_id):
        self.db_query1('SELECT age FROM Records WHERE employee_id=?;', [employee_id])
        global default_employee_age
        default_employee_age = data1

    def default_salary(self, employee_id):
        self.db_query1('SELECT salary FROM Records WHERE employee_id=?;', [employee_id])
        global default_employee_salary
        default_employee_salary = data1
    
    def default_increment(self, employee_id):
        self.db_query1('SELECT increment FROM Records WHERE employee_id=?;', [employee_id]) 
        global default_employee_increment
        default_employee_increment = data1

    def default_experience(self, employee_id):
        self.db_query1('SELECT experience_in_years FROM Records WHERE employee_id=?;', [employee_id])
        global default_employee_experience
        default_employee_experience = data1

    def default_email_id(self, employee_id):
        self.db_query1('SELECT email_id FROM Records WHERE employee_id=?;', [employee_id])
        global default_employee_email_id
        default_employee_email_id = data1

    def default_mobile_no(self, employee_id):
        self.db_query1('SELECT mobile_no FROM Records WHERE employee_id=?;', [employee_id])
        global default_employee_mobile_no
        default_employee_mobile_no = data1
    
    def default_address(self, employee_id):
        self.db_query1('SELECT address FROM Address WHERE employee_id=?;', [employee_id])
        global default_employee_address
        default_employee_address = data1

    def default_state(self, employee_id):
        self.db_query1('SELECT state FROM Address WHERE employee_id=?;', [employee_id])
        global default_employee_state
        default_employee_state = data1

    def default_id1(self, employee_name):
        self.db_query1('SELECT employee_id FROM Records WHERE employee_name=?;', [employee_name])
        global default_employee_id1
        default_employee_id1 = data1

    def default_age1(self, employee_name):
        self.db_query1('SELECT age FROM Records WHERE employee_name=?;', [employee_name])
        global default_employee_age1
        default_employee_age1 = data1

    def default_salary1(self, employee_name):
        self.db_query1('SELECT salary FROM Records WHERE employee_name=?;', [employee_name])
        global default_employee_salary1
        default_employee_salary1 = data1
    
    def default_increment1(self, employee_name):
        self.db_query1('SELECT increment FROM Records WHERE employee_name=?;', [employee_name])  
        global default_employee_increment1
        default_employee_increment1 = data1

    def default_experience1(self, employee_name):
        self.db_query1('SELECT experience_in_years FROM Records WHERE employee_name=?;', [employee_name])
        global default_employee_experience1
        default_employee_experience1 = data1

    def default_email_id1(self, employee_name):
        self.db_query1('SELECT email_id FROM Records WHERE employee_name=?;', [employee_name])
        global default_employee_email_id1
        default_employee_email_id1 = data1

    def default_mobile_no1(self, employee_name):
        self.db_query1('SELECT mobile_no FROM Records WHERE employee_name=?;', [employee_name])
        global default_employee_mobile_no1
        default_employee_mobile_no1 = data1

    def default_address1(self, employee_name):
        self.db_query1('SELECT address FROM Address WHERE employee_name=?;', [employee_name])
        global default_employee_address1
        default_employee_address1 = data1

    def default_state1(self, employee_name):
        self.db_query1('SELECT state FROM Address WHERE employee_name=?;', [employee_name])
        global default_employee_state1
        default_employee_state1 = data1

    def check_employee_id(self, employee_id):
        self.db_query('SELECT employee_id FROM Records WHERE employee_id=?;', [employee_id])
        global check_id
        check_id = data
        if len(check_id) == 0:
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + '] ' + Fore.YELLOW + " Entered Employee Id Doesn't Exist !!!")
            exit()
   
    def check_employee_name(self, employee_name):
        self.db_query('SELECT employee_id FROM Records WHERE employee_name=?;', [employee_name])
        global check_id
        check_id = data
        if len(check_id) == 0:
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + '] ' + Fore.YELLOW + " Entered Employee Name Doesn't Exist !!!")
            exit()
        
    def check_mobile_no(self, mobile_no):
        if len(str(mobile_no)) != 10 :
           print('\n[' + Fore.YELLOW + '!' + Fore.RESET + ']' +Fore.YELLOW + " Phone Number must be 10 Digits !!!" + Fore.RESET)   
           exit()

    def check_retirement_age(self, age):
        if int(age) > 59:
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + ']' +Fore.YELLOW + " Age Exceeded the Retirement Age  !!!" + Fore.RESET)   
            exit()
        elif int(age) < 18:
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + ']' +Fore.YELLOW + " Child Labouring is Illegal and It should be Punished !!!" + Fore.RESET) 
            exit()

    def order_by_id(self):
        self.db_query('SELECT * FROM Records ORDER BY employee_id;')
        print(Fore.YELLOW + "Ordered View :\n" + Fore.RESET)
        print(tabulate(data, headers=['Employee Id', 'Employee Name', 'Age', 'Salary', 'Increment','Experience (in Years)' , 'Email Id (Not Compulsary)', 'Mobile No.'], tablefmt='psql'))
      
    def order_by_name(self):
        self.db_query('SELECT * FROM Records ORDER BY employee_name;')
        print(Fore.YELLOW + "Ordered View :\n" + Fore.RESET)
        print(tabulate(data, headers=['Employee Id', 'Employee Name', 'Age', 'Salary', 'Increment','Experience (in Years)' , 'Email Id (Not Compulsary)', 'Mobile No.'], tablefmt='psql'))
        
    def order_by_age(self):
        self.db_query('SELECT * FROM Records ORDER BY age;')
        print(Fore.YELLOW + "Ordered View :\n" + Fore.RESET)
        print(tabulate(data, headers=['Employee Id', 'Employee Name', 'Age', 'Salary', 'Increment','Experience (in Years)' , 'Email Id (Not Compulsary)', 'Mobile No.'], tablefmt='psql'))
        
    def order_by_salary(self):
        self.db_query('SELECT * FROM Records ORDER BY salary DESC;')
        print(Fore.YELLOW + "Ordered View :\n" + Fore.RESET)
        print(tabulate(data, headers=['Employee Id', 'Employee Name', 'Age', 'Salary', 'Increment','Experience (in Years)' , 'Email Id (Not Compulsary)', 'Mobile No.'], tablefmt='psql'))
     
    def order_by_experience(self):
        self.db_query('SELECT * FROM Records ORDER BY experience_in_years DESC;')
        print(Fore.YELLOW + "Ordered View :\n" + Fore.RESET)
        print(tabulate(data, headers=['Employee Id', 'Employee Name', 'Age', 'Salary', 'Increment','Experience (in Years)' , 'Email Id (Not Compulsary)', 'Mobile No.'], tablefmt='psql'))
        
   
    def order_by_increment(self):
        self.db_query('SELECT * FROM Records ORDER BY increment DESC;')
        print(Fore.YELLOW + "Ordered View :\n" + Fore.RESET)
        print(tabulate(data, headers=['Employee Id', 'Employee Name', 'Age', 'Salary', 'Increment','Experience (in Years)' , 'Email Id (Not Compulsary)', 'Mobile No.'], tablefmt='psql'))
        
    def order_by_mobile_no(self):
        self.db_query('SELECT * FROM Records ORDER BY mobile_no;')
        print(Fore.YELLOW + "Ordered View :\n" + Fore.RESET)
        print(tabulate(data, headers=['Employee Id', 'Employee Name', 'Age', 'Salary', 'Increment','Experience (in Years)' , 'Email Id (Not Compulsary)', 'Mobile No.'], tablefmt='psql'))
          

                
class Search(DatabaseWrapper):
    
    def __init__(self):
        super().__init__(db_path)
        
    def search_id(self, search_by_id):
        self.db_query('SELECT * FROM Records WHERE employee_id=?;', [search_by_id])
        if len(data) == 0:
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + '] ' + Fore.YELLOW + " No Records found for the Employee Id !!!" + Fore.RESET)
            exit()
        Records().clear_screen()
        print(Fore.YELLOW + "Search Result :\n" + Fore.RESET)
        print(tabulate(data, headers=['Employee Id', 'Employee Name', 'Age', 'Salary', 'Increment','Experience (in Years)' , 'Email Id ( Not Compulsary)', 'Mobile No.'], tablefmt='psql'))


    def search_name(self, search_by_name ):
        self.db_query('SELECT * FROM Records WHERE employee_name=?;', [search_by_name])
        if len(data) == 0:
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + '] ' + Fore.YELLOW + " No Records found for the Employee Name !!!" + Fore.RESET)
            exit()
        Records().clear_screen()
        print(Fore.YELLOW + "Search Result :\n" + Fore.RESET)
        print(tabulate(data, headers=['Employee Id', 'Employee Name', 'Age', 'Salary', 'Increment','Experience (in Years)' , 'Email Id ( Not Compulsary)', 'Mobile No.'], tablefmt='psql'))


    def search_age(self, search_by_age ):
        self.db_query('SELECT * FROM Records WHERE age=?;', [search_by_age])
        if len(data) == 0:
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + '] ' + Fore.YELLOW + " No Records found for that Age !!!" + Fore.RESET)
            exit()
        Records().clear_screen()
        print(Fore.YELLOW + "Search Result :\n" + Fore.RESET)
        print(tabulate(data, headers=['Employee Id', 'Employee Name', 'Age', 'Salary', 'Increment','Experience (in Years)' , 'Email Id ( Not Compulsary)', 'Mobile No.'], tablefmt='psql'))


    def search_experience(self, search_by_experience):
        self.db_query('SELECT * FROM Records WHERE experience_in_years=?;', [search_by_experience])
        if len(data) == 0:
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + '] ' + Fore.YELLOW + " No Records found for that Experience !!!" + Fore.RESET)
            exit()
        Records().clear_screen()
        print(Fore.YELLOW + "Search Result :\n" + Fore.RESET)
        print(tabulate(data, headers=['Employee Id', 'Employee Name', 'Age', 'Salary', 'Increment','Experience (in Years)' , 'Email Id ( Not Compulsary)', 'Mobile No.'], tablefmt='psql'))

    def search_salary(self, search_by_salary):
        self.db_query('SELECT * FROM Records WHERE salary=?;', [search_by_salary])
        if len(data) == 0:
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + '] ' + Fore.YELLOW + " No Records found for that Salary !!!" + Fore.RESET)
            exit()
        Records().clear_screen()
        print(Fore.YELLOW + "Search Result :\n" + Fore.RESET)
        print(tabulate(data, headers=['Employee Id', 'Employee Name', 'Age', 'Salary', 'Increment','Experience (in Years)' , 'Email Id ( Not Compulsary)', 'Mobile No.'], tablefmt='psql'))


    def search_mobile_no(self, search_by_mobile_no):
        self.db_query('SELECT * FROM Records WHERE mobile_no=?;', [search_by_mobile_no])
        if len(data) == 0:
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + '] ' + Fore.YELLOW + " No Records found for that Mobile No. !!!" + Fore.RESET)
            exit()
        Records().clear_screen()
        print(Fore.YELLOW + "Search Result :\n" + Fore.RESET)
        print(tabulate(data, headers=['Employee Id', 'Employee Name', 'Age', 'Salary', 'Increment','Experience (in Years)' , 'Email Id ( Not Compulsary)', 'Mobile No.'], tablefmt='psql'))


    def search_by_increment(self, search_by_increment):
        self.db_query('SELECT * FROM Records WHERE imcrement=?;', [search_by_increment])
        if len(data) == 0:
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + '] ' + Fore.YELLOW + " No Records found for that Increment !!!" + Fore.RESET)
            exit()
        Records().clear_screen()
        print(Fore.YELLOW + "Search Result :\n" + Fore.RESET)
        print(tabulate(data, headers=['Employee Id', 'Employee Name', 'Age', 'Salary', 'Increment','Experience (in Years)' , 'Email Id ( Not Compulsary)', 'Mobile No.'], tablefmt='psql'))



if __name__ == '__main__':
    
    Records().clear_screen()
    print('''
        ███████╗███╗   ███╗██████╗ ██╗      ██████╗ ██╗   ██╗███████╗███████╗                               
        ██╔════╝████╗ ████║██╔══██╗██║     ██╔═══██╗╚██╗ ██╔╝██╔════╝██╔════╝                               
        █████╗  ██╔████╔██║██████╔╝██║     ██║   ██║ ╚████╔╝ █████╗  █████╗                                 
        ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██║   ██║  ╚██╔╝  ██╔══╝  ██╔══╝                                 
        ███████╗██║ ╚═╝ ██║██║     ███████╗╚██████╔╝   ██║   ███████╗███████╗                               
        ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝                               
                                                                                                    
                ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗███╗   ███╗███████╗███╗   ██╗████████╗
                ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
                ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
                ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
                ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
                ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
                                                                                                    
                           ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗                               
                           ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║                               
                           ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║                               
                           ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║                               
                           ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║                               
                           ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝                                                                                                                                                                   
    ''')
    print("      |> " + Fore.YELLOW + "    Enter 1 to Create Table [Not needed If Table has Already been Created]\n" + Fore.RESET)
    print("      |> " + Fore.YELLOW + "    Enter 2 to View All Records\n" + Fore.RESET)
    print("      |> " + Fore.YELLOW + "    Enter 3 to Add new employee records\n" + Fore.RESET) 
    print("      |> " + Fore.YELLOW + "    Enter 4 to Delete All data\n" + Fore.RESET)
    print("      |> " + Fore.YELLOW + "    Enter 5 to Delete an Employee's Record\n" + Fore.RESET)
    print("      |> " + Fore.YELLOW + "    Enter 6 to Search in Records\n" + Fore.RESET)
    print("      |> " + Fore.YELLOW + "    Enter 7 to Update Employee's Records\n" + Fore.RESET)
    print("      |> " + Fore.YELLOW + "    Enter 8 to Delete Table\n" + Fore.RESET)
    print("      |> " + Fore.YELLOW + "    Enter 9 to Order Records\n" + Fore.RESET)
    print("      |> " + Fore.YELLOW + "    Enter 10 to exit\n" + Fore.RESET)
    choice = input(Fore.YELLOW + "\nPlease Enter any no: " + Fore.RESET)
    Records().assign_description(choice)
    try:
        Records().add_changes(description2)
    except:
        do_nothing = ''
    if choice == '1':
        Records().clear_screen()
        print(Fore.GREEN + '''
            ______                __
           / ____/___ ___  ____  / /___  __  _____  ___                          
          / __/ / __ `__ \/ __ \/ / __ \/ / / / _ \/ _ \                         
         / /___/ / / / / / /_/ / / /_/ / /_/ /  __/  __/                         
        /_____/_/ /_/ /_/ .___/_/\____/\__, /\___/\___/                          
                 __  __/_/            /____/                              __     
                /  |/  /___ _____  ____ _____ ____  ____ ___  ___  ____  / /_    
               / /|_/ / __ `/ __ \/ __ `/ __ `/ _ \/ __ `__ \/ _ \/ __ \/ __/    ''' + Fore.YELLOW  + '''
              / /  / / /_/ / / / / /_/ / /_/ /  __/ / / / / /  __/ / / / /_      
             /_/  /_/\__,_/_/ /_/\__,_/\__, /\___/_/ /_/ /_/\___/_/ /_/\__/      
                       _____          /____/                                     
                      / ___/__  _______/ /____  ____ ___                         
                      \__ \/ / / / ___/ __/ _ \/ __ `__ \                        
                     ___/ / /_/ (__  ) /_/  __/ / / / / /                        
                    /____/\__, /____/\__/\___/_/ /_/ /_/                         
                         /____/                                                  

        ''' + Fore.RESET )
        Records().create_table()
        description = 'Database Tables were successfully created'
        Records().add_changes(description)
        print('[' + Fore.YELLOW + '!' + Fore.RESET + '] ' + Fore.YELLOW + ' Successfully Created Database !!!')
        Records().rerun_program()
    elif choice == '2':
        Records().clear_screen()
        print(Fore.MAGENTA + '''
         _______  __   __  _______  ___      _______  __   __  _______  _______                       
        |       ||  |_|  ||       ||   |    |       ||  | |  ||       ||       |                      
        |    ___||       ||    _  ||   |    |   _   ||  |_|  ||    ___||    ___|                      
        |   |___ |       ||   |_| ||   |    |  | |  ||       ||   |___ |   |___                       
        |    ___||       ||    ___||   |___ |  |_|  ||_     _||    ___||    ___|                      
        |   |___ | ||_|| ||   |    |       ||       |  |   |  |   |___ |   |___                       
        |_______||_|   |_||___|    |_______||_______|  |___|  |_______||_______|                      
                   __   __  _______  __    _  _______  _______  _______  __   __  _______  __    _  _______ 
                  |  |_|  ||   _   ||  |  | ||   _   ||       ||       ||  |_|  ||       ||  |  | ||       |
                  |       ||  |_|  ||   |_| ||  |_|  ||    ___||    ___||       ||    ___||   |_| ||_     _|
                  |       ||       ||       ||       ||   | __ |   |___ |       ||   |___ |       |  |   |  
                  |       ||       ||  _    ||       ||   ||  ||    ___||       ||    ___||  _    |  |   |  
                  | ||_|| ||   _   || | |   ||   _   ||   |_| ||   |___ | ||_|| ||   |___ | | |   |  |   |  
                  |_|   |_||__| |__||_|  |__||__| |__||_______||_______||_|   |_||_______||_|  |__|  |___|  
                             _______  __   __  _______  _______  _______  __   __                                 
                            |       ||  | |  ||       ||       ||       ||  |_|  |                                
                            |  _____||  |_|  ||  _____||_     _||    ___||       |                                
                            | |_____ |       || |_____   |   |  |   |___ |       |                                
                            |_____  ||_     _||_____  |  |   |  |    ___||       |                                
                             _____| |  |   |   _____| |  |   |  |   |___ | ||_|| |                                
                            |_______|  |___|  |_______|  |___|  |_______||_|   |_|                                                                 
                                                                                                     '                                                                             
        ''' + Fore.RESET)
        Records().check_table_exists()
        print("      |> " + Fore.YELLOW + "    Enter 1 to View Employee's Office Records\n" + Fore.RESET)
        print("      |> " + Fore.YELLOW + "    Enter 2 to View Employee's Addresses\n" + Fore.RESET)
        print("      |> " + Fore.YELLOW + "    Enter 3 to Exit\n" + Fore.RESET) 
        view_choice = input(Fore.YELLOW + "\nPlease Enter any No. : ")
        if view_choice == '1':
            Records().clear_screen()
            print(Fore.YELLOW + 'Records:\n' + Fore.RESET)
            Records().view_all_data()
            description = 'All Office Records were Viewed'
            Records().add_changes(description)
            Records().rerun_program()
        elif view_choice == '2':
            Records().clear_screen()
            print(Fore.YELLOW + 'Records:\n' + Fore.RESET)
            Records().view_address_data()
            description = 'All Employee Address Records were Viewed'
            Records().add_changes(description)
            Records().rerun_program()
    elif choice == '3':
        Records().clear_screen()
        print(Fore.CYAN + '''
        / ()             |\  _        _  _                      
        >-   /|/|/|  |/\_|/ / \_|  | |/ |/                      
        \___/ | | |_/|_/ |_/\_/  \/|/|_/|_/                     
              ,_ _  (|            (|                            
             /| | |   _,         _,   _,  _          _      _|_ 
              | | |  / |  /|/|  / |  / | |/ /|/|/|  |/ /|/|  |  
              | | |_/\/|_/ | |_/\/|_/\/|/|_/ | | |_/|_/ | |_/|_/
                                      (|                   
                    ()       , _|_  _                         
                    /\ |  | / \_|  |/ /|/|/|                    
                   /(_) \/|/ \/ |_/|_/ | | |_/                  
                         (|                                     
        ''' + Fore.RESET)
        Records().check_table_exists()
        employee_id = input(Fore.YELLOW + 'Enter the Employee Id : ' + Fore.RESET)
        Records().check_add_employee_value(employee_id)
        employee_name = input(Fore.YELLOW + "\nEnter the Employee's Name: " + Fore.RESET)
        Records().check_add_employee_value(employee_name)
        age = input(Fore.YELLOW + "\nEnter the Employee's age: " + Fore.RESET)
        Records().check_add_employee_value(age)
        Records().check_retirement_age(age)
        salary = input(Fore.YELLOW + "\nEnter the Employee's salary: "+ Fore.RESET)
        Records().check_add_employee_value(salary)
        increment = input(Fore.YELLOW + "\nEnter the Employee's yearly Increment: " + Fore.RESET)
        Records().check_add_employee_value(increment)
        experience_in_years = input(Fore.YELLOW + "\nEnter the Employee's Experience in Your Company: " + Fore.RESET)
        Records().check_add_employee_value(experience_in_years)
        email_id = input(Fore.YELLOW + "\nEnter the Employee's Email-Id: " + Fore.RESET)
        Records().check_add_employee_value(email_id)
        mobile_no = input(Fore.YELLOW + "\nEnter the Employee's Mobile No. : " + Fore.RESET)
        Records().check_add_employee_value(mobile_no)
        Records().check_mobile_no(mobile_no)
        address = input(Fore.YELLOW + "\nEnter the Employee's Address : " + Fore.RESET)
        Records().check_add_employee_value(address)
        state = input(Fore.YELLOW + "\nEnter the Employee's State and Country : ")
        Records().check_add_employee_value(state)
        Records().add_employee(employee_id ,employee_name ,age ,salary ,increment ,experience_in_years ,email_id ,mobile_no)
        Records().add_employee_address(employee_id ,employee_name ,address ,state)
        print("\n[" + Fore.YELLOW + "!" + Fore.RESET + "]" + Fore.YELLOW + " Successfully Added Employee Records!!!")
        description = 'New Record with Employee Id ' + employee_id + ' was Added'
        Records().add_changes(description)
        Records().rerun_program()
    elif choice == '4':
        Records().clear_screen()
        print(Fore.RED + '''
         ___            _
        | __|_ __  _ __| |___ _  _ ___ ___                   
        | _|| '  \| '_ \ / _ \ || / -_) -_)                  
        |___|_|_|_| .__/_\___/\_, \___\___|             _    
          |  \/  ||_|_ _ _  __|__/_ _ ___ _ __  ___ _ _| |_  
          | |\/| / _` | ' \/ _` / _` / -_) '  \/ -_) ' \  _| 
          |_| _|_\__,_|_||_\__,_\__, \___|_|_|_\___|_||_\__| 
             / __|_  _ __| |_ __|___/_                       
             \__ \ || (_-<  _/ -_) '  \                      
             |___/\_, /__/\__\___|_|_|_|                     
                  |__/                                  
        ''' + Fore.RESET)
        Records().check_table_exists1()
        Records().magic_word_authentication()
        Records().clear_data()
        description = 'All Records data was Deleted'
        Records().add_changes(description)
        Records().rerun_program()
    elif choice == '5':
        Records().clear_screen()
        print(Fore.RED + '''
         _______             _
        (_______)           | |                                             
         _____   ____  ____ | | ___  _   _  ____ ____                       
        |  ___) |    \|  _ \| |/ _ \| | | |/ _  ) _  )                      
        | |_____| | | | | | | | |_| | |_| ( (/ ( (/ /                       
        |_______)_|_|_| ||_/|_|\___/ \__  |\____)____)                      
                      |_|           (____/                                  
              ______                                                         
             |  ___ \                                                 _      
             | | _ | | ____ ____   ____  ____  ____ ____   ____ ____ | |_    
             | || || |/ _  |  _ \ / _  |/ _  |/ _  )    \ / _  )  _ \|  _)   
             | || || ( ( | | | | ( ( | ( ( | ( (/ /| | | ( (/ /| | | | |__   
             |_||_||_|\_||_|_| |_|\_||_|\_|| |\____)_|_|_|\____)_| |_|\___)  
                                       (_____|                               
                      _                                                     
                     | |              _                                     
                      \ \  _   _  ___| |_  ____ ____                        
                       \ \| | | |/___)  _)/ _  )    \                       
                   _____) ) |_| |___ | |_( (/ /| | | |                      
                  (______/ \__  (___/ \___)____)_|_|_|                      
                          (____/                                     

        ''' + Fore.RESET)
        Records().check_table_exists1()
        Records().magic_word_authentication()
        employee_id = input(Fore.YELLOW + "\nPlease Enter the Employee Id to Delete : " + Fore.RESET)
        Records().check_add_employee_value(employee_id)
        Records().check_employee_id(employee_id)
        Records().clear_employee_data(employee_id)
        description = "Record with Employee Id " + employee_id + ' was Deleted'
        Records().add_changes(description)
        Records().rerun_program()
    elif choice == '6':
        Records().clear_screen()
        print('''
         ██████████                        ████                                                                            
        ░░███░░░░░█                       ░░███                                                                            
         ░███  █ ░ █████████████  ████████ ░███   ██████  █████ ████ ██████  ██████                                        
         ░██████  ░░███░░███░░███░░███░░███░███  ███░░███░░███ ░███ ███░░██████░░███                                       
         ░███░░█   ░███ ░███ ░███ ░███ ░███░███ ░███ ░███ ░███ ░███░███████░███████                                        
         ░███ ░   █░███ ░███ ░███ ░███ ░███░███ ░███ ░███ ░███ ░███░███░░░ ░███░░░                                         
         ███████████████░███ █████░███████ █████░░██████  ░░███████░░██████░░██████                                        
        ░░░░░░░░░░░░░░░ ░░░ ░░░░░ ░███░░░ ░░░░░  ░░░░░░    ░░░░░███ ░░░░░░  ░░░░░░                                         
                                  ░███                     ███ ░███                                                        
                ██████   ██████    █████                   ░░██████                                                 █████   
               ░░██████ ██████    ░░░░░                     ░░░░░░                                                 ░░███    
                ░███░█████░███   ██████  ████████    ██████    ███████  ██████  █████████████    ██████  ████████  ███████  
                ░███░░███ ░███  ░░░░░███░░███░░███  ░░░░░███  ███░░███ ███░░███░░███░░███░░███  ███░░███░░███░░███░░░███░   
                ░███ ░░░  ░███   ███████ ░███ ░███   ███████ ░███ ░███░███████  ░███ ░███ ░███ ░███████  ░███ ░███  ░███    
                ░███      ░███  ███░░███ ░███ ░███  ███░░███ ░███ ░███░███░░░   ░███ ░███ ░███ ░███░░░   ░███ ░███  ░███ ███
                █████     █████░░████████████ █████░░████████░░███████░░██████  █████░███ █████░░██████  ████ █████ ░░█████ 
                ░░░░░     ░░░░░  ░░░░░░░░░░░░ ░░░░░  ░░░░░░░░  ░░░░░███ ░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░  ░░░░ ░░░░░   ░░░░░  
                                                               ███ ░███                                                      
                           █████████                  █████   ░░██████                                                       
                         ███░░░░░███                ░░███     ░░░░░░                                                        
                        ░███    ░░░ █████ ████ ████████████    ██████  █████████████                                        
                        ░░█████████░░███ ░███ ███░░░░░███░    ███░░███░░███░░███░░███                                       
                         ░░░░░░░░███░███ ░███░░█████ ░███    ░███████  ░███ ░███ ░███                                       
                         ███    ░███░███ ░███ ░░░░███░███ ███░███░░░   ░███ ░███ ░███                                       
                        ░░█████████ ░░███████ ██████ ░░█████ ░░██████  █████░███ █████                                      
                         ░░░░░░░░░   ░░░░░███░░░░░░   ░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░                                       
                                     ███ ░███                                                                               
                                    ░░██████                                                                                
                                      ░░░░░░                                                                            ''')
        Records().check_table_exists()
        print("      |> " + Fore.YELLOW + "    Enter 1 to Search By Employee Id\n" + Fore.RESET)
        print("      |> " + Fore.YELLOW + "    Enter 2 to Search By Employee Name\n" + Fore.RESET)
        print("      |> " + Fore.YELLOW + "    Enter 3 to Search By Age\n" + Fore.RESET) 
        print("      |> " + Fore.YELLOW + "    Enter 4 to Search By Salary\n" + Fore.RESET)
        print("      |> " + Fore.YELLOW + "    Enter 5 to Search By Experience\n" + Fore.RESET)
        print("      |> " + Fore.YELLOW + "    Enter 6 to Search By Increment\n" + Fore.RESET)
        print("      |> " + Fore.YELLOW + "    Enter 7 to Search By Mobile No.\n" + Fore.RESET)
        print("      |> " + Fore.YELLOW + "    Enter 8 to exit\n" + Fore.RESET)
        search_choice = input(Fore.YELLOW + 'Please Enter any no. : ' + Fore.RESET)
        if search_choice == '1':
            search_by_id = input(Fore.YELLOW + '\nEnter the Id to Search : ' + Fore.RESET)
            Records().check_add_employee_value(search_by_id)
            Records().check_employee_id(search_by_id)
            Search().search_id(search_by_id)
            description = 'Records with Employee Id "' + search_by_id + '" was Searched'
            Records().add_changes(description)
            Records().rerun_program()  
        elif search_choice == '2':
            search_by_name = input(Fore.YELLOW + '\nEnter the Name to Search : ' + Fore.RESET)
            Records().check_add_employee_value(search_by_name)
            Search().search_name(search_by_name)
            description = 'Records with Employee Name "' + search_by_name + '" was Searched'
            Records().add_changes(description)
            Records().rerun_program()
        elif search_choice == '3':
            search_by_age = input(Fore.YELLOW + '\nEnter the Age to Search : ' + Fore.RESET)
            Records().check_add_employee_value(search_by_age)
            Records().check_retirement_age(search_by_age)
            Search().search_age(search_by_age)
            description = 'Records with Employee Age "' + search_by_age + '" was Searched'
            Records().add_changes(description)
            Records().rerun_program()
        elif search_choice == '4':
            search_by_salary = input(Fore.YELLOW + '\nEnter the Salary to Search : ' + Fore.RESET)
            Records().check_add_employee_value(search_by_salary)
            Search().search_salary(search_by_salary)
            description = 'Records with Employee Salary "' + search_by_salary + '" was Searched'
            Records().add_changes(description)
            Records().rerun_program()
        elif search_choice == '5':
            search_by_experience = input(Fore.YELLOW + '\nEnter the Experience of the Employee to Search : ' + Fore.RESET)
            Records().check_add_employee_value(search_by_experience)
            Search().search_experience(search_by_experience)
            description = 'Records with Experience "' + search_by_experience + ' years" was Searched'
            Records().add_changes(description)
            Records().rerun_program()
        elif search_choice == '6':
            search_by_increment = input(Fore.YELLOW + '\nEnter the Increment to Search : ' + Fore.RESET)
            Records().check_add_employee_value(search_by_increment)
            Search().search_increment(search_by_increment)
            description = 'Records with Increment "$' + search_by_increment + '" was Searched'
            Records().add_changes(description)
            Records().rerun_program()
        elif search_choice == '7':
            search_by_mobile_no = input(Fore.YELLOW + '\nEnter the Mobile No. to Search : ' + Fore.RESET)
            Records().check_add_employee_value(search_by_mobile_no)
            Records().check_mobile_no()    
            Search().search_mobile_no(search_by_mobile_no)
            description = 'Records with Mobile No. "+91 ' + search_by_mobile_no + '" was Searched'
            Records().add_changes(description)
            Records().rerun_program()
        else:
            exit()
    elif choice == '7':
        Records().clear_screen()
        print('''
        ╔═╗┌┬┐┌─┐┬  ┌─┐┬ ┬┌─┐┌─┐  ╔╦╗┌─┐┌┐┌┌─┐┌─┐┌─┐┌┬┐┌─┐┌┐┌┌┬┐  ╔═╗┬ ┬┌─┐┌┬┐┌─┐┌┬┐
        ║╣ │││├─┘│  │ │└┬┘├┤ ├┤   ║║║├─┤│││├─┤│ ┬├┤ │││├┤ │││ │   ╚═╗└┬┘└─┐ │ ├┤ │││
        ╚═╝┴ ┴┴  ┴─┘└─┘ ┴ └─┘└─┘  ╩ ╩┴ ┴┘└┘┴ ┴└─┘└─┘┴ ┴└─┘┘└┘ ┴   ╚═╝ ┴ └─┘ ┴ └─┘┴ ┴
        ''')
        Records().check_table_exists()
        print("      |> " + Fore.YELLOW + "    Enter 1 to Update Record By Employee Id\n" + Fore.RESET)
        print("      |> " + Fore.YELLOW + "    Enter 2 to Update Record By Employee Name\n" + Fore.RESET) 
        print("      |> " + Fore.YELLOW + "    Enter 3 to Exit\n" + Fore.RESET)
        update_choice = input(Fore.YELLOW + 'Please Enter any no. : ' + Fore.RESET)
        if update_choice == '1':
            employee_id = input(Fore.YELLOW + '\nEnter the Employee Id to Update : ' + Fore.RESET)
            Records().check_add_employee_value(employee_id)
            Records().check_employee_id(employee_id)
            Records().default_name(employee_id)
            employee_name = input(Fore.YELLOW + "\nEnter the New Employee's Name : " + Fore.RESET) or default_employee_name
            Records().default_age(employee_id)
            age = input(Fore.YELLOW + "\nEnter the New Employee's age : " + Fore.RESET) or default_employee_age
            Records().check_retirement_age(age)
            Records().default_salary(employee_id)
            salary = input(Fore.YELLOW + "\nEnter the New Employee's salary : " + Fore.RESET) or default_employee_salary
            Records().default_increment(employee_id)
            increment = input(Fore.YELLOW + "\nEnter the New Employee's yearly Increment : " + Fore.RESET) or default_employee_increment
            Records().default_experience(employee_id)
            experience_in_years = input(Fore.YELLOW + "\nEnter the New Employee's Experience in Your Company : " + Fore.RESET) or default_employee_experience
            Records().default_email_id(employee_id)
            email_id = input(Fore.YELLOW + "\nEnter the New Employee's Email-Id : " + Fore.RESET) or default_employee_email_id
            Records().default_mobile_no(employee_id)
            mobile_no = input(Fore.YELLOW + "\nEnter the New Employee's Mobile No. :" + Fore.RESET) or default_employee_mobile_no
            Records().check_mobile_no(mobile_no)
            Records().default_address(employee_id)
            address = input(Fore.YELLOW + "\nEnter the New Employee's Address :" + Fore.RESET) or default_employee_address
            Records().default_state(employee_id)
            state = input(Fore.YELLOW + "\nEnter the New State & Country :" + Fore.RESET) or default_employee_state
            Records().update_data_id(employee_id, employee_name, age, salary, increment, experience_in_years, email_id, mobile_no, address, state)
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + ']' +Fore.YELLOW + "Choosen Records are Updated Successfully !!!")
            description = 'Record with Employee Id ' + employee_id + ' was Updated'
            Records().add_changes(description)
            Records().rerun_program()
        elif update_choice == '2':
            employee_name = input(Fore.YELLOW + '\nEnter the Employee Name to Update : ' + Fore.RESET)
            Records().check_add_employee_value(employee_name)
            Records().check_employee_name(employee_name)
            Records().default_id1(employee_name)
            employee_id = input(Fore.YELLOW + "\nEnter the New Employee's Id : " + Fore.RESET) or default_employee_id1
            Records().default_age1(employee_name)
            age = input(Fore.YELLOW + "\nEnter the New Employee's age : " + Fore.RESET) or default_employee_age1
            Records().check_retirement_age(age)
            Records().default_salary1(employee_name)
            salary = input(Fore.YELLOW + "\nEnter the New Employee's salary : " + Fore.RESET) or default_employee_salary1
            Records().default_increment1(employee_name)
            increment = input(Fore.YELLOW + "\nEnter the New Employee's yearly Increment : " + Fore.RESET) or default_employee_increment1
            Records().default_experience1(employee_name)
            experience_in_years = input(Fore.YELLOW + "\nEnter the New  Employee's Experience in Your Company : " + Fore.RESET) or default_employee_experience1
            Records().default_email_id1(employee_name)
            email_id = input(Fore.YELLOW + "\nEnter the New Employee's Email-Id : " + Fore.RESET) or default_employee_email_id1
            Records().default_mobile_no1(employee_name)
            mobile_no = input(Fore.YELLOW + "\nEnter the New Employee's Mobile No. :" + Fore.RESET) or default_employee_mobile_no1
            Records().check_mobile_no()
            Records().default_address1(employee_name)
            address = input(Fore.YELLOW + "\nEnter the New Employee's Address :" + Fore.RESET) or default_employee_address1
            Records().default_state(employee_name)
            state = input(Fore.YELLOW + "\nEnter the New State & Country :" + Fore.RESET) or default_employee_state1
            Records().update_data_name(employee_id, employee_name, age, salary, increment, experience_in_years, email_id, mobile_no, address, state)
            print('\n[' + Fore.YELLOW + '!' + Fore.RESET + ']' +Fore.YELLOW + "Choosen Records are Updated Successfully !!!")
            description = 'Records with Employee Name ' + employee_name + ' was Updated'
            Records().add_changes(description)
            Records().rerun_program()            
        else:
            exit() 
    elif choice == '8':
        Records().clear_screen()
        print('''
        ▓█████  ███▄ ▄███▓ ██▓███   ██▓     ▒█████ ▓██   ██▓▓█████ ▓█████                                    
        ▓█   ▀ ▓██▒▀█▀ ██▒▓██░  ██▒▓██▒    ▒██▒  ██▒▒██  ██▒▓█   ▀ ▓█   ▀                                    
        ▒███   ▓██    ▓██░▓██░ ██▓▒▒██░    ▒██░  ██▒ ▒██ ██░▒███   ▒███                                      
        ▒▓█  ▄ ▒██    ▒██ ▒██▄█▓▒ ▒▒██░    ▒██   ██░ ░ ▐██▓░▒▓█  ▄ ▒▓█  ▄                                    
        ░▒████▒▒██▒   ░██▒▒██▒ ░  ░░██████▒░ ████▓▒░ ░ ██▒▓░░▒████▒░▒████▒                                   
        ░░ ▒░ ░░ ▒░   ░  ░▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░   ██▒▒▒ ░░ ▒░ ░░░ ▒░ ░                                   
         ░ ░  ░░  ░      ░░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░ ▓██ ░▒░  ░ ░  ░ ░ ░  ░                                   
           ░   ░      ░   ░░         ░ ░   ░ ░ ░ ▒  ▒ ▒ ░░     ░      ░                                      
           ░  ░       ░                ░  ░    ░ ░  ░ ░        ░  ░   ░  ░                                   
                                            ░ ░                                                      
                ███▄ ▄███▓ ▄▄▄       ███▄    █  ▄▄▄        ▄████ ▓█████  ███▄ ▄███▓▓█████  ███▄    █ ▄▄▄█████▓
               ▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ ▒████▄     ██▒ ▀█▒▓█   ▀ ▓██▒▀█▀ ██▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒
               ▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██  ▀█▄  ▒██░▄▄▄░▒███   ▓██    ▓██░▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░
               ▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄ ▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
               ▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░ ▓█   ▓██▒░▒▓███▀▒░▒████▒▒██▒   ░██▒░▒████▒▒██░   ▓██░  ▒██▒ ░ 
               ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   
               ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░  ░   ░  ░ ░  ░░  ░      ░ ░ ░  ░░ ░░   ░ ▒░    ░    
               ░      ░     ░   ▒      ░   ░ ░   ░   ▒   ░ ░   ░    ░   ░      ░      ░      ░   ░ ░   ░      
                      ░         ░  ░         ░       ░  ░      ░    ░  ░       ░      ░  ░         ░          
                                                                                                     
                          ██████▓██   ██▓  ██████ ▄▄▄█████▓▓█████  ███▄ ▄███▓                                 
                        ▒██    ▒ ▒██  ██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██▒▀█▀ ██▒                                 
                        ░ ▓██▄    ▒██ ██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██    ▓██░                                 
                          ▒   ██▒ ░ ▐██▓░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██    ▒██                                  
                        ▒██████▒▒ ░ ██▒▓░▒██████▒▒  ▒██▒ ░ ░▒████▒▒██▒   ░██▒                                 
                        ▒ ▒▓▒ ▒ ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒░   ░  ░                                 
                        ░ ░▒  ░ ░▓██ ░▒░ ░ ░▒  ░ ░    ░     ░ ░  ░░  ░      ░                                 
                        ░  ░  ░  ▒ ▒ ░░  ░  ░  ░    ░         ░   ░      ░                                    
                              ░  ░ ░           ░              ░  ░       ░                                    
                                 ░ ░                                                                          ''')
        Records().check_table_exists1()
        Records().magic_word_authentication()
        Records().delete_table()  
        Records().add_changes(description1)
        Records().rerun_program()  
    elif choice == '9':
        Records().clear_screen()
        print(Fore.BLUE + '''
         _______  ___      ___    _______   ___        ______  ___  ___  _______   _______    
        /"     "||"  \    /"  |  |   __ "\ |"  |      /    " \|"  \/"  |/"     "| /"     "|                                                
       (: ______) \   \  //   |  (. |__) :)||  |     // ____  \    \  /(: ______)(: ______)                                                
        \/    |   /\   \/.    |  |:  ____/ |:  |    /  /    ) :)\   \/  \/    |   \/    |                                                  
        // ___)_ |: \.        |  (|  /      \  |___(: (____/ // /   /   // ___)_  // ___)_                                                 
       (:      "||.  \    /:  | /|__/ \    ( \_|:  \         / /   /   (:      "|(:      "|                                                
        \_______)|___|\__/|___|(_______)    \_______)\ _____/ |___/     \_______) \_______)                                                
                                                                                                                                    
                 ___      ___       __      _____  ___        __       _______    _______  ___      ___   _______  _____  ___  ___________  
                |"  \    /"  |     /""\    (\    \|"  \      /""\     /" _   "|  /"     "||"  \    /"  | /"     "|(\    \|"  \("     _   ") 
                 \   \  //   |    /    \   |.\    \    |    /    \   (: ( \___) (: ______) \   \  //   |(: ______)|.\    \    |)__/  \ __/  
                 /\   \/.    |   /' /\  \  |: \.   \   |   /' /\  \   \/ \       \/    |   /\   \/.    | \/    |  |: \.   \   |   \ _ /     
                |: \.        |  //  __'  \ |.  \    \. |  //  __'  \  //  \ ___  // ___)_ |: \.        | // ___)_ |.  \    \. |   |.  |     
                |.  \    /:  | /   /  \   \|    \    \ | /   /  \   \(:   _(  _|(:      "||.  \    /:  |(:      "||    \    \ |   \:  |     
                |___|\__/|___|(___/    \___)\___|\____\)(___/    \___)\_______)  \_______)|___|\__/|___| \_______) \___|\____\)    \__|     
                                                                                                                                    
                            ________  ___  ___  ________  ___________  _______  ___      ___                                                  
                           /"       )|"  \/"  |/"       )("     _   ")/"     "||"  \    /"  |                                                 
                          (:   \___/  \   \  /(:   \___/  )__/  \ __/(: ______) \   \  //   |                                                 
                           \___  \     \   \/  \___  \       \ _ /    \/    |   /\   \/.    |                                                 
                            __/   \    /   /    __/   \      |.  |    // ___)_ |: \.        |                                                 
                           /" \   :)  /   /    /" \   :)     \:  |   (:      "||.  \    /:  |                                                 
                          (_______/  |___/    (_______/       \__|    \_______)|___|\__/|___|                                                 
                                                                                                                                                          
        ''' + Fore.RESET)
        print("      |> " + Fore.YELLOW + "    Enter 1 to Order by Employee's Id\n" + Fore.RESET)
        print("      |> " + Fore.YELLOW + "    Enter 2 to Order By Employee Name\n" + Fore.RESET)
        print("      |> " + Fore.YELLOW + "    Enter 3 to Order By Age\n" + Fore.RESET) 
        print("      |> " + Fore.YELLOW + "    Enter 4 to Order By Salary\n" + Fore.RESET)
        print("      |> " + Fore.YELLOW + "    Enter 5 to Order By Experience\n" + Fore.RESET)
        print("      |> " + Fore.YELLOW + "    Enter 6 to Order By Increment\n" + Fore.RESET)
        print("      |> " + Fore.YELLOW + "    Enter 7 to Order By Mobile No.\n" + Fore.RESET)
        print("      |> " + Fore.YELLOW + "    Enter 8 to exit\n" + Fore.RESET)
        order_choice = input(Fore.YELLOW + 'Please Enter any no. : ' + Fore.RESET)
        if order_choice == '1':
            Records().clear_screen()
            Records().order_by_id()
            description = 'All Records were Viewed in Employee Id Order'
            Records().add_changes(description)
            Records().rerun_program()
        elif order_choice == '2':
            Records().clear_screen()
            Records().order_by_name()
            description = 'All Records were Viewed in Employee Name Order'
            Records().add_changes(description)
            Records().rerun_program()
        elif order_choice == '3':
            Records().clear_screen()
            Records().order_by_age()
            description = 'All Records were Viewed in Employee Age Order'
            Records().add_changes(description)
            Records().rerun_program()
        elif order_choice == '4':
            Records().clear_screen()
            Records().order_by_salary()
            description = 'All Records were Viewed in Salary Order'
            Records().add_changes(description)
            Records().rerun_program()
        elif order_choice == '5':
            Records().clear_screen()
            Records().order_by_experience()
            description = 'All Records were Viewed in Experience Order'
            Records().add_changes(description)
            Records().rerun_program()
        elif order_choice == '6':
            Records().clear_screen()
            Records().order_by_increment()
            description = 'All Records were Viewed in Increment Order'
            Records().add_changes(description)
            Records().rerun_program()
        elif order_choice == '7':
            Records().clear_screen()
            Records().order_by_mobile_no()
            description = 'All Records were Viewed in Mobile No. Order'
            Records().add_changes(description)
            Records().rerun_program()
        else:
            exit()
    elif choice == 'thisisunstoppable':
        Records().clear_screen()
        Records().magic_word_authentication()
        Records().clear_screen()
        Records().view_secret_table()
        description = 'Changes Table was Viewed'
        Records().add_changes(description)
        Records().rerun_program()
    else:
        exit()
                





















import tkinter 
from tkinter.ttk import *
from tkinter import *
import sqlite3
from constant import db_path
from os import *
from tabulate import tabulate
from colorama import Fore





window = tkinter.Tk()
window.title("Employee Management System")
window.geometry('1366x768')
window.configure(background='black')



class DatabaseWrapper:

    def __init__(self, db_name):
        self.db_name = db_name

    def db_query(self, cmd, args=[], fetchone=True):
        database = sqlite3.connect(self.db_name)
        sql = database.cursor().execute(cmd, args)
        global data
        data = sql.fetchall()
        database.close()
        return data

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


class Home(DatabaseWrapper):
    def __init__(self):
        super().__init__(db_path)

    def home_delete_page(self):
        black_screen2.destroy()
        black_screen1.destroy()
        successfully_deleted.destroy()
        home_button2.destroy()
        delete_the_table.destroy()
        self.patch()
   
    def home_table_page(self):
        successfully_created.destroy()
        home_button1.destroy()

    def home_add_page(self):
        successfully_created2.destroy()
        black_screen4.destroy()
        home_button3.destroy()

    def delete_all_page(self):
        successfully_deleted1.destroy()
        home_button4.destroy()
 
    def delete_employee_page(self):
        successfully_deleted2.destroy()
        home_button5.destroy()
 
    def delete_employee_page2(self):
        black_screen5.destroy()
        employee_management_system1.destroy()
        employee_id_button1.destroy()

    def delete_window_page(self):
        black_screen1.destroy()
        home_button10.destroy()

    def search_id_page(self):
        black_screen7.destroy()
        employee_management_system2.destroy()
        employee_id_button1.destroy()

    def search_name_page(self):
        black_screen10.destroy()
        employee_management_system3.destroy()
        employee_name_button1.destroy()

    def search_age_page(self):
        black_screen12.destroy()
        employee_management_system4.destroy()
        employee_age_button1.destroy()

    def search_salary_page(self):
        black_screen14.destroy()
        employee_management_system6.destroy()
        employee_salary_button1.destroy()

    def search_increment_page(self):
        black_screen16.destroy()
        employee_management_system8.destroy()
        employee_increment_button1.destroy()

    def search_mobile_no_page(self):
        black_screen18.destroy()
        employee_management_system10.destroy()
        employee_mobile_no_button1.destroy()

    def update_page(self):
        black_screen20.destroy()
        home_button11.destroy()

    def update_id_page(self):
        employee_management_system21.destroy()
        black_screen21.destroy()
        employee_id_button3.destroy()
    
    def update_id_page1(self):
        black_screen22.destroy()

    def update_name_page(self):
        employee_management_system23.destroy()
        black_screen25.destroy()
        employee_name_button3.destroy()

    def update_name_page1(self):
        black_screen26.destroy()
   
    def update_success_page(self):
        black_screen23.destroy()
        home_button5.destroy()
        successfully_updated1.destroy()

    def update_success_page1(self):
        black_screen27.destroy()
        home_button6.destroy()
        successfully_updated2.destroy()\

    def add_employee_page(self):
        black_screen4.destroy()
   
    def view_table_page(self):
        black_screen3.destroy()
        employee_management_system3.destroy()
        home_button7.destroy()
        employee_name_heading.destroy()
        employee_id_heading.destroy()
        employee_age_heading.destroy()
        employee_salary_heading.destroy()
        employee_increment_heading.destroy()
        employee_experience_heading.destroy()
        employee_email_id_heading.destroy()
        employee_mobile_no_heading.destroy()

    def search_id_page1(self):
        employee_name_heading.destroy()
        employee_id_heading.destroy()
        employee_age_heading.destroy()
        employee_salary_heading.destroy()
        employee_increment_heading.destroy()
        employee_experience_heading.destroy()
        employee_email_id_heading.destroy()
        employee_mobile_no_heading.destroy()
        employee_management_system3.destroy()
        black_screen8.destroy()
        home_button8.destroy()

    def search_name_page1(self):
        employee_name_heading.destroy()
        employee_id_heading.destroy()
        employee_age_heading.destroy()
        employee_salary_heading.destroy()
        employee_increment_heading.destroy()
        employee_experience_heading.destroy()
        employee_email_id_heading.destroy()
        employee_mobile_no_heading.destroy()
        employee_management_system4.destroy()
        black_screen11.destroy()
        home_button12.destroy()
    
    def search_age_page1(self):
        employee_name_heading.destroy()
        employee_id_heading.destroy()
        employee_age_heading.destroy()
        employee_salary_heading.destroy()
        employee_increment_heading.destroy()
        employee_experience_heading.destroy()
        employee_email_id_heading.destroy()
        employee_mobile_no_heading.destroy()
        employee_management_system5.destroy()
        black_screen13.destroy()
        home_button13.destroy()

    
    def search_salary_page1(self):
        employee_name_heading.destroy()
        employee_id_heading.destroy()
        employee_age_heading.destroy()
        employee_salary_heading.destroy()
        employee_increment_heading.destroy()
        employee_experience_heading.destroy()
        employee_email_id_heading.destroy()
        employee_mobile_no_heading.destroy()
        employee_management_system7.destroy()
        black_screen15.destroy()
        home_button14.destroy()
  
    def search_increment_page1(self):
        employee_name_heading.destroy()
        employee_id_heading.destroy()
        employee_age_heading.destroy()
        employee_salary_heading.destroy()
        employee_increment_heading.destroy()
        employee_experience_heading.destroy()
        employee_email_id_heading.destroy()
        employee_mobile_no_heading.destroy()
        employee_management_system9.destroy()
        black_screen17.destroy()
        home_button15.destroy()  
    
    def search_mobile_no_page1(self):
        employee_name_heading.destroy()
        employee_id_heading.destroy()
        employee_age_heading.destroy()
        employee_salary_heading.destroy()
        employee_increment_heading.destroy()
        employee_experience_heading.destroy()
        employee_email_id_heading.destroy()
        employee_mobile_no_heading.destroy()
        employee_management_system11.destroy()
        black_screen19.destroy()
        home_button16.destroy()

    def search_page(self):
        black_screen6.destroy()
        home_button9.destroy()

    def patch(self):
        table_exists = 'y'
        try:
            Record().check_table_exist()
        except:
            global no_table
            no_table = Label(window, text="Database Tables doesn't Exist or Not been Created !!! ", width=400, bd=0, height=25, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            no_table.place(x=700, y=450)
            no_table.pack(side=BOTTOM,anchor='center', padx=200, pady=7)
            table_exists = 'n'
        if table_exists == 'y':
            delete_something = tkinter.Button(window, text="Delete Records",command=Window().delete_window, bg='#FFFACD', fg='black', width=20, height=2, font=('TeX Gyre Adventor',14,"normal"))
            delete_something.place(x=580, y=320)
            add_employee = tkinter.Button(window, text="Add Employee",command=Window().add_employee_window, bg='#FFFACD', fg='black', width=20, height=2, font=('TeX Gyre Adventor',14,"normal"))
            add_employee.place(x=580, y=220)
            view_all_records = tkinter.Button(window, text="View Records", command=Window().view_table_window, bg='#FFFACD', fg='black', width=20, height=2, font=('TeX Gyre Adventor',14,"normal"))
            view_all_records.place(x=580, y=420)
            search_something = tkinter.Button(window, text="Search Records", command=Window().search_window, bg='#FFFACD', fg='black', width=20, height=2, font=('TeX Gyre Adventor',14,"normal"))
            search_something.place(x=580, y=520)
            update_something = tkinter.Button(window, text="Update Records", command=Window().update_window, bg='#FFFACD', fg='black', width=20, height=2, font=('TeX Gyre Adventor',14,"normal"))
            update_something.place(x=580, y=620)

class Record(DatabaseWrapper):
     
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
        try:
            no_table.destroy()
            Home().patch()
        except:
            print()
        global successfully_created
        successfully_created = tkinter.Label(window, text="Successfully Created Database Tables !!!", fg='white', bg='black', width=300, height=300, font=('TeX Gyre Adventor',20,"normal"))
        successfully_created.pack()
        global home_button1
        home_button1 = tkinter.Button(text="Back", command=lambda: Home().home_table_page(), bg='#FFFACD', fg='black', width=8, height=2, font=('TeX Gyre Adventor',14,"normal"))
        home_button1.place(x=1190, y=640)


    def delete_table(self):
        self.db_execute('DROP TABLE Records;')
        black_screen1.destroy()
        home_button10.destroy()
        global black_screen2
        black_screen2 = tkinter.Frame(window, width=1280, height=720, bg="black")
        black_screen2.pack(fill=tkinter.BOTH, expand=True)
        global successfully_deleted
        successfully_deleted = tkinter.Label(black_screen2, text="Successfully Deleted Database Tables !!!", fg='white', bg='black', width=300, height=300, font=('TeX Gyre Adventor',20,"normal"))
        successfully_deleted.place(x=100, y=200)
        successfully_deleted.pack()
        global home_button2
        home_button2 = tkinter.Button(text="Home", command=lambda: Home().home_delete_page(), bg='#FFFACD', fg='black', width=10, height=2, font=('TeX Gyre Adventor',14,"normal"))
        home_button2.place(x=1190, y=640)

    def add_employee(self ,employee_id ,employee_name ,age ,salary ,increment ,experience_in_years ,email_id ,mobile_no):
        self.db_execute('''
        INSERT INTO Records(employee_id ,employee_name ,age ,salary ,increment ,experience_in_years ,email_id ,mobile_no)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?);''', args=[employee_id, employee_name, age, salary, increment, experience_in_years, email_id, mobile_no])
        black_screen4.destroy()
        global successfully_created2
        successfully_created2 = tkinter.Label(window, text="Successfully Added to Records !!!", fg='white', bg='black', width=300, height=300, font=('TeX Gyre Adventor',20,"normal"))
        successfully_created2.pack()
        global home_button3
        home_button3 = tkinter.Button(text="Home", command=Home().home_add_page, bg='#FFFACD', fg='black', width=10, height=2, font=('TeX Gyre Adventor',14,"normal"))
        home_button3.place(x=1190, y=640)       
 
    def delete_all_data(self):
        self.db_execute('DELETE FROM Records;') 
        black_screen1.destroy()   
        home_button10.destroy()
        global successfully_deleted1
        successfully_deleted1 = tkinter.Label(window, text="Successfully Deleted All Records !!!", fg='white', bg='black', width=300, height=300, font=('TeX Gyre Adventor',20,"normal"))
        successfully_deleted1.pack()
        global home_button4
        home_button4 = tkinter.Button(text="Home", command=Home().delete_all_page, bg='#FFFACD', fg='black', width=10, height=2, font=('TeX Gyre Adventor',14,"normal"))
        home_button4.place(x=1190, y=640) 

    def delete_an_employee_data(self, employee_id):
        employee_management_system1.destroy()
        self.db_execute('DELETE FROM Records WHERE employee_id=?;', [employee_id]) 
        black_screen5.destroy() 
        employee_id_button1.destroy()  
        global successfully_deleted2
        successfully_deleted2 = tkinter.Label(window, text="Successfully Deleted the Chosen Record !!!", fg='white', bg='black', width=300, height=300, font=('TeX Gyre Adventor',20,"normal"))
        successfully_deleted2.pack()
        global home_button5
        home_button5 = tkinter.Button(text="Home", command=Home().delete_employee_page, bg='#FFFACD', fg='black', width=10, height=2, font=('TeX Gyre Adventor',14,"normal"))
        home_button5.place(x=1190, y=640) 

    def delete_employee_data(self):
        employee_id = employee_id_entry1.get()
        self.db_query('SELECT * FROM Records WHERE employee_id=?;', [employee_id])
        if len(employee_id) == 0:
            enter_text1 = Label(black_screen5, text="Please Enter a Value !!! ", width=32, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text1.place(x=925, y=0)
            enter_text1.pack(side=RIGHT, align='UP', padx=20, pady=7)
        elif len(data) == 0:
            emp_exist1 = Label(black_screen5, text="Employee Id doesn't Exist !!! ", width=32, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            emp_exist1.place(x=925, y=0)
            emp_exist1.pack(side=RIGHT,align='UP', padx=20, pady=7)
        else:
            self.delete_an_employee_data(employee_id)
    def table_buttons(self):
        global employee_id_heading
        employee_id_heading = tkinter.Button(window, text="Employee's Id", width=14, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',14,'normal'))    
        employee_id_heading.place(x=11, y=80)
        global employee_name_heading
        employee_name_heading = tkinter.Button(window, text="Employee Name", width=14, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',14,'normal'))    
        employee_name_heading.place(x=179, y=80)
        global employee_age_heading
        employee_age_heading = tkinter.Button(window, text="Age", width=14, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',14,'normal'))    
        employee_age_heading.place(x=347, y=80)
        global employee_salary_heading
        employee_salary_heading = tkinter.Button(window, text="Salary", width=14, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',14,'normal'))    
        employee_salary_heading.place(x=514, y=80)
        global employee_increment_heading
        employee_increment_heading = tkinter.Button(window, text="Increment", width=14, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',14,'normal'))    
        employee_increment_heading.place(x=683, y=80)
        global employee_experience_heading
        employee_experience_heading = tkinter.Button(window, text="Experience", width=14, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',14,'normal'))    
        employee_experience_heading.place(x=851, y=80)
        global employee_email_id_heading
        employee_email_id_heading = tkinter.Button(window, text="Email Id", width=14, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',14,'normal'))    
        employee_email_id_heading.place(x=1019, y=80)
        global employee_mobile_no_heading
        employee_mobile_no_heading = tkinter.Button(window, text="Mobile No.", width=14, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',14,'normal'))    
        employee_mobile_no_heading.place(x=1186, y=80)   
       
    def search_id(self):
        employee_id = employee_id_entry2.get()
        self.db_query('SELECT * FROM Records WHERE employee_id=?;', [employee_id])
        if len(employee_id) == 0:
            enter_text1 = Label(black_screen7, text="Please Enter a Value !!! ", width=32, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text1.place(x=925, y=0)
            enter_text1.pack(side=RIGHT, align='UP', padx=20, pady=7)
        elif len(data) == 0:
            emp_exist1 = Label(black_screen7, text="Employee Id doesn't Exist !!! ", width=32, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            emp_exist1.place(x=925, y=0)
            emp_exist1.pack(side=RIGHT, align='UP', padx=20, pady=7)
        else:
            black_screen7.destroy()
            employee_id_button1.destroy()
            employee_management_system2.destroy()
            global employee_management_system3
            employee_management_system3 = tkinter.Label(text="", fg='white', bg='black', width=40, height=0)
            employee_management_system3.pack()
            global black_screen8
            black_screen8 = tkinter.Frame(height=1000, width=1000, bg='black')
            black_screen8.pack(fill=tkinter.Y, expand=True)
            self.table_buttons()
            global home_button8
            home_button8 = Button(text="Home",command=lambda: Home().search_id_page1(), width=8, height=0, fg='black', bg='#FFFACD', font=('TeX Gyre Adventor',14,'normal'))
            home_button8.place(x=1200, y=30)
            '''scroll_bar = Scrollbar()
            scroll_bar.pack(side=RIGHT, align=UP)'''
            total_rows = len(data)
            total_columns = len(data[0])
            for i in range(total_rows): 
                for j in range(total_columns):   
                    view_tables = Entry(black_screen8, width=18, fg='white', bg='black', font=('Latin Modern Mono Slanted',13,'normal'))    
                    view_tables.grid(row=i, column=j, sticky='news') 
                    view_tables.insert(END, data[i][j]) 

    def search_name(self):
        employee_name = employee_name_entry2.get()
        self.db_query('SELECT * FROM Records WHERE employee_name=?;', [employee_name])
        if len(employee_name) == 0:
            enter_text1 = Label(black_screen10, text="Please Enter a Value !!! ", width=40, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text1.place(x=925, y=0)
            enter_text1.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(data) == 0:
            emp_exist1 = Label(black_screen10, text="No Records Found for the Given Name !!! ", width=40, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            emp_exist1.place(x=925, y=0)
            emp_exist1.pack(side=RIGHT, align='UP', padx=200, pady=7)
        else:
            employee_management_system3.destroy()
            employee_name_button1.destroy()
            black_screen10.destroy()
            global employee_management_system4
            employee_management_system4 = tkinter.Label(text="", fg='white', bg='black', width=40, height=0)
            employee_management_system4.pack()
            global black_screen11
            black_screen11 = tkinter.Frame(height=1000, width=1000, bg='black')
            black_screen11.pack(fill=tkinter.Y, expand=True)
            global home_button12
            home_button12 = Button(text="Home",command=lambda: Home().search_name_page1(), width=8, height=0, fg='black', bg='#FFFACD', font=('TeX Gyre Adventor',14,'normal'))
            home_button12.place(x=1200, y=30)
            self.table_buttons()
            total_rows = len(data)
            total_columns = len(data[0])
            for i in range(total_rows): 
                for j in range(total_columns):   
                    view_tables = Entry(black_screen11, width=18, fg='white', bg='black', font=('Latin Modern Mono Slanted',13,'normal'))    
                    view_tables.grid(row=i, column=j, sticky='news') 
                    view_tables.insert(END, data[i][j]) 
            
    def search_age(self):
        age = employee_age_entry2.get()
        self.db_query('SELECT * FROM Records WHERE age=?;', [age])
        if len(age) == 0:
            enter_text1 = Label(black_screen12, text="Please Enter a Value !!! ", width=40, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text1.place(x=925, y=0)
            enter_text1.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(data) == 0:
            emp_exist1 = Label(black_screen12, text="No Records Found for the Given Age !!! ", width=40, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            emp_exist1.place(x=925, y=0)
            emp_exist1.pack(side=RIGHT, align='UP', padx=200, pady=7)
        else:
            employee_management_system4.destroy()
            employee_age_button1.destroy()
            black_screen12.destroy()
            global employee_management_system5
            employee_management_system5 = tkinter.Label(text="", fg='white', bg='black', width=40, height=0)
            employee_management_system5.pack()
            global black_screen13
            black_screen13 = tkinter.Frame(height=1000, width=1000, bg='black')
            black_screen13.pack(fill=tkinter.Y, expand=True)
            global home_button13
            home_button13 = Button(text="Home",command=lambda: Home().search_age_page1(), width=8, height=0, fg='black', bg='#FFFACD', font=('TeX Gyre Adventor',14,'normal'))
            home_button13.place(x=1200, y=30)
            self.table_buttons()
            total_rows = len(data)
            total_columns = len(data[0])
            for i in range(total_rows): 
                for j in range(total_columns):   
                    view_tables = Entry(black_screen13, width=18, fg='white', bg='black', font=('Latin Modern Mono Slanted',13,'normal'))    
                    view_tables.grid(row=i, column=j, sticky='news') 
                    view_tables.insert(END, data[i][j]) 

    def search_salary(self):
        salary = employee_salary_entry2.get()
        self.db_query('SELECT * FROM Records WHERE salary=?;', [salary])
        if len(salary) == 0:
            enter_text1 = Label(black_screen14, text="Please Enter a Value !!! ", width=40, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text1.place(x=925, y=0)
            enter_text1.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(data) == 0:
            emp_exist1 = Label(black_screen14, text="No Records Found for the Given Salary !!! ", width=40, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            emp_exist1.place(x=925, y=0)
            emp_exist1.pack(side=RIGHT, align='UP', padx=200, pady=7)
        else:
            employee_management_system6.destroy()
            employee_salary_button1.destroy()
            black_screen14.destroy()
            global employee_management_system7
            employee_management_system7 = tkinter.Label(text="", fg='white', bg='black', width=40, height=0)
            employee_management_system7.pack()
            global black_screen15
            black_screen15 = tkinter.Frame(height=1000, width=1000, bg='black')
            black_screen15.pack(fill=tkinter.Y, expand=True)
            global home_button14
            home_button14 = Button(text="Home",command=lambda: Home().search_salary_page1(), width=8, height=0, fg='black', bg='#FFFACD', font=('TeX Gyre Adventor',14,'normal'))
            home_button14.place(x=1200, y=30)
            self.table_buttons()
            total_rows = len(data)
            total_columns = len(data[0])
            for i in range(total_rows): 
                for j in range(total_columns):   
                    view_tables = Entry(black_screen15, width=18, fg='white', bg='black', font=('Latin Modern Mono Slanted',13,'normal'))    
                    view_tables.grid(row=i, column=j, sticky='news') 
                    view_tables.insert(END, data[i][j]) 

    def search_increment(self):
        increment = employee_increment_entry2.get()
        self.db_query('SELECT * FROM Records WHERE increment=?;', [increment])
        if len(increment) == 0:
            enter_text1 = Label(black_screen16, text="Please Enter a Value !!! ", width=40, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text1.place(x=925, y=0)
            enter_text1.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(data) == 0:
            emp_exist1 = Label(black_screen16, text="No Records Found for the Given Increment !!! ", width=40, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            emp_exist1.place(x=925, y=0)
            emp_exist1.pack(side=RIGHT, align='UP', padx=200, pady=7)
        else:
            employee_management_system8.destroy()
            employee_increment_button1.destroy()
            black_screen16.destroy()
            global employee_management_system9
            employee_management_system9 = tkinter.Label(text="", fg='white', bg='black', width=40, height=0)
            employee_management_system9.pack()
            global black_screen17
            black_screen17 = tkinter.Frame(height=1000, width=1000, bg='black')
            black_screen17.pack(fill=tkinter.Y, expand=True)
            global home_button15
            home_button15 = Button(text="Home",command=lambda: Home().search_increment_page1(), width=8, height=0, fg='black', bg='#FFFACD', font=('TeX Gyre Adventor',14,'normal'))
            home_button15.place(x=1200, y=30)
            self.table_buttons()
            total_rows = len(data)
            total_columns = len(data[0])
            for i in range(total_rows): 
                for j in range(total_columns):   
                    view_tables = Entry(black_screen17, width=18, fg='white', bg='black', font=('Latin Modern Mono Slanted',13,'normal'))    
                    view_tables.grid(row=i, column=j, sticky='news') 
                    view_tables.insert(END, data[i][j]) 

    def search_mobile_no(self):
        mobile_no = employee_mobile_no_entry2.get()
        self.db_query('SELECT * FROM Records WHERE mobile_no=?;', [mobile_no])
        if len(mobile_no) == 0:
            enter_text1 = Label(black_screen18, text="Please Enter a Value !!! ", width=40, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text1.place(x=925, y=0)
            enter_text1.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(data) == 0:
            emp_exist1 = Label(black_screen18, text="No Records Found for the Given Mobile No. !!! ", width=40, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            emp_exist1.place(x=925, y=0)
            emp_exist1.pack(side=RIGHT, align='UP', padx=200, pady=7)
        else:
            employee_management_system10.destroy()
            employee_mobile_no_button1.destroy()
            black_screen18.destroy()
            global employee_management_system11
            employee_management_system11 = tkinter.Label(text="", fg='white', bg='black', width=40, height=0)
            employee_management_system11.pack()
            global black_screen19
            black_screen19 = tkinter.Frame(height=1000, width=1000, bg='black')
            black_screen19.pack(fill=tkinter.Y, expand=True)
            global home_button16
            home_button16 = Button(text="Home",command=lambda: Home().search_mobile_no_page1(), width=8, height=0, fg='black', bg='#FFFACD', font=('TeX Gyre Adventor',14,'normal'))
            home_button16.place(x=1200, y=30)
            self.table_buttons()
            total_rows = len(data)
            total_columns = len(data[0])
            for i in range(total_rows): 
                for j in range(total_columns):   
                    view_tables = Entry(black_screen19, width=18, fg='white', bg='black', font=('Latin Modern Mono Slanted',13,'normal'))    
                    view_tables.grid(row=i, column=j, sticky='news') 
                    view_tables.insert(END, data[i][j]) 

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

    def check_employee_id(self, employee_id):
        self.db_query('SELECT employee_id FROM Records WHERE employee_id=?;', [employee_id])
        global check_id
        check_id = data
 
    def check_mobile_no(self, mobile_no):
        self.db_query1('SELECT * FROM Records WHERE mobile_no=?', [mobile_no])
        global check_mobile_no
        check_mobile_no = data1
 
    def check_table_exist(self):
        self.db_query('SELECT * FROM Records;')

    def add_value_checker1(self):
        try:
            enter_text12.destroy()
        except:
            print()
        try:
            enter_text13.destroy()
        except:
            print()
        try:
            enter_text14.destroy()
        except:
            print()
        try:
            enter_text15.destroy()
        except:
            print()
        try:
            enter_text16.destroy()
        except:
            print()
        try:
            enter_text17.destroy()
        except:
            print()
        try:
            enter_text18.destroy()
        except:
            print()
        try:
            enter_text19.destroy()
        except:
            print()
        try:
            enter_text20.destroy()
        except:
            print()

    def update_id(self, employee_id):
        self.add_value_checker1()
        employee_id = employee_id_entry1.get()
        employee_name = employee_name_entry1.get()
        age = employee_age_entry1.get()
        salary = employee_salary_entry1.get()
        increment = employee_increment_entry1.get()
        experience_in_years = employee_experience_entry1.get()
        email_id = employee_email_id_entry1.get()
        mobile_no = employee_mobile_no_entry1.get()
        global enter_text12
        global enter_text13
        global enter_text14
        global enter_text15
        global enter_text16
        global enter_text17
        global enter_text18
        global enter_text19
        global enter_text20
        if len(employee_id) == 0:
            self.add_value_checker1()
            enter_text12 = Label(black_screen22, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text12.place(x=820, y=0)
            enter_text12.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(employee_name) == 0:
            self.add_value_checker1()
            enter_text13 = Label(black_screen22, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text13.place(x=820, y=35)
            enter_text13.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(age) == 0:
            self.add_value_checker1()
            enter_text14 = Label(black_screen22, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text14.place(x=820, y=70)
            enter_text14.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(salary) == 0:
            self.add_value_checker1()
            enter_text15 = Label(black_screen22, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text15.place(x=820, y=110)
            enter_text15.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(increment) == 0:
            self.add_value_checker1()
            enter_text16 = Label(black_screen22, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text16.place(x=820, y=145)
            enter_text16.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(experience_in_years) == 0:
            self.add_value_checker1()
            enter_text17 = Label(black_screen22, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text17.place(x=820, y=185)
            enter_text17.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(email_id) == 0:
            self.add_value_checker1()
            enter_text18 = Label(black_screen22, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text18.place(x=820, y=220)
            enter_text18.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(mobile_no) == 0:
            self.add_value_checker1()
            enter_text19 = Label(black_screen22, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text19.place(x=820, y=255)
            enter_text19.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(mobile_no) != 10 and len(mobile_no) != 0:
            self.add_value_checker1()
            enter_text20 = Label(black_screen22, text="Phone Number Must be 10 digits !!! ", width=30, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text20.place(x=820, y=255)
            enter_text20.pack(side=RIGHT, align='UP', padx=200, pady=7)
        else:
            self.db_execute('''
            UPDATE Records
            SET employee_id=?, employee_name=?, age=?, salary=?, increment=?, experience_in_years=?, email_id=?, mobile_no=?
            WHERE employee_id=?;''', args=[employee_id, employee_name, age, salary, increment, experience_in_years, email_id, mobile_no, employee_id])
            black_screen22.destroy()
            global black_screen23
            black_screen23 = tkinter.Frame(window, width=1000, height=1000, bg="black")
            black_screen23.pack(fill=tkinter.BOTH, expand=True)
            global successfully_updated1
            successfully_updated1 = tkinter.Label(black_screen23, text="Successfully Updated the Chosen Record !!!", fg='white', bg='black', width=300, height=300, font=('TeX Gyre Adventor',20,"normal"))
            successfully_updated1.pack()
            global home_button5
            home_button5 = tkinter.Button(text="Home", command=Home().update_success_page, bg='#FFFACD', fg='black', width=10, height=2, font=('TeX Gyre Adventor',14,"normal"))
            home_button5.place(x=1190, y=640) 

    def add_value_checker2(self):
        try:
            enter_text21.destroy()
        except:
            print()
        try:
            enter_text22.destroy()
        except:
            print()
        try:
            enter_text23.destroy()
        except:
            print()
        try:
            enter_text24.destroy()
        except:
            print()
        try:
            enter_text25.destroy()
        except:
            print()
        try:
            enter_text26.destroy()
        except:
            print()
        try:
            enter_text27.destroy()
        except:
            print()
        try:
            enter_text28.destroy()
        except:
            print()
        try:
            enter_text29.destroy()
        except:
            print()
        
    def update_name(self, employee_name):
        self.add_value_checker()
        employee_id = employee_id_entry1.get()
        employee_name = employee_name_entry1.get()
        age = employee_age_entry1.get()
        salary = employee_salary_entry1.get()
        increment = employee_increment_entry1.get()
        experience_in_years = employee_experience_entry1.get()
        email_id = employee_email_id_entry1.get()
        mobile_no = employee_mobile_no_entry1.get()
        global enter_text21
        global enter_text22
        global enter_text23
        global enter_text24
        global enter_text25
        global enter_text26
        global enter_text27
        global enter_text28
        global enter_text29
        if len(employee_id) == 0:
            self.add_value_checker2()
            enter_text21 = Label(black_screen26, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text21.place(x=820, y=0)
            enter_text21.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(employee_name) == 0:
            self.add_value_checker()
            enter_text22 = Label(black_screen26, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text22.place(x=820, y=35)
            enter_text22.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(age) == 0:
            self.add_value_checker()
            enter_text23 = Label(black_screen26, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text23.place(x=820, y=70)
            enter_text23.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(salary) == 0:
            self.add_value_checker()
            enter_text24 = Label(black_screen26, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text24.place(x=820, y=110)
            enter_text24.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(increment) == 0:
            self.add_value_checker()
            enter_text25 = Label(black_screen26, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text25.place(x=820, y=145)
            enter_text25.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(experience_in_years) == 0:
            self.add_value_checker()
            enter_text26 = Label(black_screen26, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text26.place(x=820, y=185)
            enter_text26.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(email_id) == 0:
            self.add_value_checker()
            enter_text27 = Label(black_screen26, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text27.place(x=820, y=220)
            enter_text27.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(mobile_no) == 0:
            self.add_value_checker()
            enter_text28 = Label(black_screen26, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text28.place(x=820, y=255)
            enter_text28.pack(side=RIGHT, align='UP', padx=200, pady=7)
        elif len(mobile_no) != 10 and len(mobile_no) != 0:
            self.add_value_checker()
            enter_text29 = Label(black_screen26, text="Phone Number Must be 10 digits !!! ", width=30, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text29.place(x=820, y=255)
            enter_text29.pack(side=RIGHT, align='UP', padx=200, pady=7)
        else:
            self.db_execute('''
            UPDATE Records
            SET employee_id=?, employee_name=?, age=?, salary=?, increment=?, experience_in_years=?, email_id=?, mobile_no=?
            WHERE employee_name=?;''', args=[employee_id, employee_name, age, salary, increment, experience_in_years, email_id, mobile_no, employee_name])
            black_screen26.destroy()
            global black_screen27
            black_screen27 = tkinter.Frame(window, width=1000, height=1000, bg="black")
            black_screen27.pack(fill=tkinter.BOTH, expand=True)
            global successfully_updated2
            successfully_updated2 = tkinter.Label(black_screen27, text="Successfully Updated the Chosen Record !!!", fg='white', bg='black', width=300, height=300, font=('TeX Gyre Adventor',20,"normal"))
            successfully_updated2.pack()
            global home_button6
            home_button6 = tkinter.Button(text="Home", command=Home().update_success_page1, bg='#FFFACD', fg='black', width=10, height=2, font=('TeX Gyre Adventor',14,"normal"))
            home_button6.place(x=1190, y=640) 

class Window(DatabaseWrapper):

    def __init__(self):
        super().__init__(db_path)
    
    def delete_window(self):
        global black_screen1
        black_screen1 = tkinter.Frame(window, width=1280, height=800, bg="black")
        black_screen1.pack()
        global delete_the_table
        delete_the_table = tkinter.Button(black_screen1, text="     Delete Table       ",command=Record().delete_table, bg='#FFFACD', fg='black', width=24, height=2, font=('TeX Gyre Adventor',14,"normal"))
        delete_the_table.place(x=500, y=125)
        global delete_an_employee
        delete_an_employee = tkinter.Button(black_screen1, text=" Delete An Employee Record ",command=self.delete_employee_window ,bg='#FFFACD', fg='black', width=24, height=2, font=('TeX Gyre Adventor',14,"normal"))
        delete_an_employee.place(x=500, y=250)
        global delete_all_records
        delete_all_records = tkinter.Button(black_screen1, text="   Delete All Records   ",command=lambda: Record().delete_all_data()  ,bg='#FFFACD', fg='black', width=24, height=2, font=('TeX Gyre Adventor',14,"normal"))
        delete_all_records.place(x=500, y=375)
        global home_button10
        home_button10 = tkinter.Button(text="Back", command=Home().delete_window_page, bg='#FFFACD', fg='black', width=10, height=2, font=('TeX Gyre Adventor',14,"normal"))
        home_button10.place(x=1190, y=640) 

    def view_table_window(self):
        self.db_query('SELECT * FROM Records;') 
        global black_screen3 
        black_screen3 = Frame(window, height=900, width=850, bg='black')
        global home_button7
        home_button7 = Button(text="Back",command=lambda: Home().view_table_page(), width=8, height=0, fg='black', bg='#FFFACD', font=('TeX Gyre Adventor',14,'normal'))
        home_button7.place(x=1200, y=30)
        global employee_management_system3
        employee_management_system3 = tkinter.Label(text="", fg='white', bg='black', width=40, height=0)
        employee_management_system3.pack()
        black_screen3.pack(fill=tkinter.Y, expand=True)
        total_rows = len(data)
        total_columns = len(data[0])
        Record().table_buttons()
        for i in range(total_rows): 
            for j in range(total_columns): 
                view_tables = Entry(black_screen3, width=18, fg='white', bg='black', font=('Latin Modern Mono Slanted',13,'normal'))    
                view_tables.grid(row=i, column=j, sticky='news') 
                view_tables.insert(END, data[i][j]) 

    def add_employee_window(self):
        global black_screen4
        black_screen4 = tkinter.Frame(height=1000, width=1000, bg='black')
        black_screen4.pack(fill=tkinter.BOTH, expand=True)
        employee_id_button = tkinter.Button(black_screen4, text="Employee Id", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_id_button.place(x=410, y=0)
        global employee_id_entry
        employee_id_entry = Entry(black_screen4, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_id_entry.pack()  
        employee_name_button = tkinter.Button(black_screen4, text="Employee Name", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_name_button.place(x=410, y=37)
        global employee_name_entry
        employee_name_entry = Entry(black_screen4, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_name_entry.pack()
        employee_age_button = tkinter.Button(black_screen4, text="Age", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_age_button.place(x=410, y=74)
        global employee_age_entry
        employee_age_entry = Entry(black_screen4, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_age_entry.pack()
        employee_salary_button = tkinter.Button(black_screen4, text="Salary", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_salary_button.place(x=410, y=110)
        global employee_salary_entry
        employee_salary_entry = Entry(black_screen4, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_salary_entry.pack()
        employee_increment_button = tkinter.Button(black_screen4, text="Increment", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_increment_button.place(x=410, y=147)
        global employee_increment_entry
        employee_increment_entry = Entry(black_screen4, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_increment_entry.pack()
        employee_experience_button = tkinter.Button(black_screen4, text="Experience", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_experience_button.place(x=410, y=184)
        global employee_experience_entry
        employee_experience_entry = Entry(black_screen4, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_experience_entry.pack()
        employee_email_id_button = tkinter.Button(black_screen4, text="Email Id", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_email_id_button.place(x=410, y=221)
        global employee_email_id_entry
        employee_email_id_entry = Entry(black_screen4, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_email_id_entry.pack()
        employee_mobile_no_button = tkinter.Button(black_screen4, text="Mobile No.", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_mobile_no_button.place(x=410, y=258)
        global employee_mobile_no_entry
        employee_mobile_no_entry = Entry(black_screen4, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_mobile_no_entry.pack()
        
        continue_button = tkinter.Button(black_screen4, text='Continue',command=self.add_employee_records, width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        continue_button.place(x=640, y=380)
        cancel_button = tkinter.Button(black_screen4, text='Cancel',command=lambda: Home().add_employee_page(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        cancel_button.place(x=430, y=380)
        

    def add_value_checker(self):
        try:
            enter_text1.destroy()
        except:
            print()
        try:
            enter_text2.destroy()
        except:
            print()
        try:
            enter_text3.destroy()
        except:
            print()
        try:
            enter_text4.destroy()
        except:
            print()
        try:
            enter_text5.destroy()
        except:
            print()
        try:
            enter_text6.destroy()
        except:
            print()
        try:
            enter_text7.destroy()
        except:
            print()
        try:
            enter_text8.destroy()
        except:
            print()
        try:
            enter_text9.destroy()
        except:
            print()
        try:
            enter_text10.destroy()
        except:
            print()
        try:
            enter_text11.destroy()
        except:
            print()

    def add_employee_records(self):
        self.add_value_checker()
        employee_id = employee_id_entry.get()
        employee_name = employee_name_entry.get()
        age = employee_age_entry.get()
        salary = employee_salary_entry.get()
        increment = employee_increment_entry.get()
        experience_in_years = employee_experience_entry.get()
        email_id = employee_email_id_entry.get()
        mobile_no = employee_mobile_no_entry.get()
        if len(employee_id) != 0:
            Record().check_employee_id(employee_id)
        if len(mobile_no) == 10 and len(mobile_no) != 0:
            Record().check_mobile_no(mobile_no)
        global enter_text1
        global enter_text2
        global enter_text3
        global enter_text4
        global enter_text5
        global enter_text6
        global enter_text7
        global enter_text8
        global enter_text9
        global enter_text10
        global enter_text11
        if len(employee_id) == 0:
            self.add_value_checker()
            enter_text1 = Label(black_screen4, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text1.place(x=820, y=0)
            enter_text1.pack(side=RIGHT, align='UP', padx=200, pady=7)
            return
        elif len(employee_name) == 0:
            self.add_value_checker()
            enter_text2 = Label(black_screen4, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text2.place(x=820, y=35)
            enter_text2.pack(side=RIGHT, align='UP', padx=200, pady=7)
            return
        elif len(age) == 0:
            self.add_value_checker()
            enter_text3 = Label(black_screen4, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text3.place(x=820, y=70)
            enter_text3.pack(side=RIGHT, align='UP', padx=200, pady=7)
            return
        elif len(salary) == 0:
            self.add_value_checker()
            enter_text4 = Label(black_screen4, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text4.place(x=820, y=110)
            enter_text4.pack(side=RIGHT, align='UP', padx=200, pady=7)
            return
        elif len(increment) == 0:
            self.add_value_checker()
            enter_text5 = Label(black_screen4, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text5.place(x=820, y=145)
            enter_text5.pack(side=RIGHT, align='UP', padx=200, pady=7)
            return
        elif len(experience_in_years) == 0:
            self.add_value_checker()
            enter_text6 = Label(black_screen4, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text6.place(x=820, y=185)
            enter_text6.pack(side=RIGHT, align='UP', padx=200, pady=7)
            return
        elif len(email_id) == 0:
            self.add_value_checker()
            enter_text7 = Label(black_screen4, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text7.place(x=820, y=220)
            enter_text7.pack(side=RIGHT, align='UP', padx=200, pady=7)
            return
        elif len(mobile_no) == 0:
            self.add_value_checker()
            enter_text8 = Label(black_screen4, text="Please Enter a Value !!! ", width=20, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text8.place(x=820, y=255)
            enter_text8.pack(side=RIGHT, align='UP', padx=200, pady=7)
            return
        elif len(mobile_no) != 10 and len(mobile_no) != 0:
            self.add_value_checker()
            enter_text9 = Label(black_screen4, text="Phone Number Must be 10 digits !!! ", width=30, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text9.place(x=820, y=255)
            enter_text9.pack(side=RIGHT, align='UP', padx=200, pady=7)
            return
        elif len(mobile_no) == 10 and len(mobile_no) != 0:
            try:
                Record().check_mobile_no(mobile_no)
                if len(check_mobile_no) != 0:
                    self.add_value_checker()
                    enter_text11 = Label(black_screen4, text="Mobile No. Already Exists !!! ", width=30, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
                    enter_text11.place(x=820, y=255)
                    enter_text11.pack(side=RIGHT, align='UP', padx=200, pady=7)
                    return
            except:
                print()
        elif len(employee_id) != 0:
            try:
                Record().check_employee_id(employee_id)
                if len(check_id) != 0:
                    self.add_value_checker()
                    enter_text10 = Label(black_screen4, text="Employee Id Already Exists !!! ", width=30, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
                    enter_text10.place(x=820, y=0)
                    enter_text10.pack(side=RIGHT, align='UP', padx=200, pady=7)
                    return
            except:
                print()
        Record().add_employee(employee_id, employee_name, age, salary, increment, experience_in_years, email_id, mobile_no)

    def delete_employee_window(self):
        black_screen1.destroy()
        home_button10.destroy()
        global employee_management_system1
        employee_management_system1 = tkinter.Label(text="", fg='white', bg='black', width=30, height=9, font=('TeX Gyre Adventor',20,"bold"))
        employee_management_system1.pack()
        global black_screen5
        black_screen5 = tkinter.Frame(height=1000, width=1000, bg='black')
        black_screen5.pack(fill=tkinter.BOTH, expand=True)
        global employee_id_entry1
        employee_id_entry1 = Entry(black_screen5, width=40, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_id_entry1.pack(side=TOP)  
        global employee_id_button1
        employee_id_button1 = tkinter.Button(text="Enter the Employee Id to Delete :", width=32, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_id_button1.place(x=520, y=291)
        continue_button = tkinter.Button(black_screen5, text='Continue',command=lambda: Record().delete_employee_data(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        continue_button.place(x=840, y=170)
        cancel_button = tkinter.Button(black_screen5, text='Cancel',command=lambda: Home().delete_employee_page2(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        cancel_button.place(x=300, y=170)

    def search_window(self):
        global black_screen6
        black_screen6 = tkinter.Frame(height=1000, width=1000, bg='black')
        black_screen6.pack(fill=tkinter.BOTH, expand=True)
        search_by_id = tkinter.Button(black_screen6, text="Search By Id", command=self.search_id_window , bg='#FFFACD', fg='black', width=20, height=2, font=('TeX Gyre Adventor',14,"normal"))
        search_by_id.place(x=580, y=0)
        search_by_name = tkinter.Button(black_screen6, text="Search By Name", command=self.search_name_window , bg='#FFFACD', fg='black', width=20, height=2, font=('TeX Gyre Adventor',14,"normal"))
        search_by_name.place(x=580, y=100)
        search_by_age = tkinter.Button(black_screen6, text="Search By Age",command=self.search_age_window, bg='#FFFACD', fg='black', width=20, height=2, font=('TeX Gyre Adventor',14,"normal"))
        search_by_age.place(x=580, y=200)
        search_by_salary = tkinter.Button(black_screen6, text="Search By Salary",command=self.search_salary_window, bg='#FFFACD', fg='black', width=20, height=2, font=('TeX Gyre Adventor',14,"normal"))
        search_by_salary.place(x=580, y=300)
        search_by_increment = tkinter.Button(black_screen6, text="Search By Increment",command=self.search_increment_window, bg='#FFFACD', fg='black', width=20, height=2, font=('TeX Gyre Adventor',14,"normal"))
        search_by_increment.place(x=580, y=400)
        search_by_mobile_no = tkinter.Button(black_screen6, text="Search By Mobile No.",command=self.search_mobile_no_window, bg='#FFFACD', fg='black', width=20, height=2, font=('TeX Gyre Adventor',14,"normal"))
        search_by_mobile_no.place(x=580, y=500)
        global home_button9
        home_button9 = tkinter.Button(text="Back", command=Home().search_page, bg='#FFFACD', fg='black', width=10, height=2, font=('TeX Gyre Adventor',14,"normal"))
        home_button9.place(x=1190, y=640) 


    def search_id_window(self):
        black_screen6.destroy()
        home_button9.destroy()
        global employee_management_system2
        employee_management_system2 = tkinter.Label(text="", fg='white', bg='black', width=38, height=8, font=('TeX Gyre Adventor',20,"bold"))
        employee_management_system2.pack()
        global black_screen7
        black_screen7 = tkinter.Frame(height=1000, width=1000, bg='black')
        black_screen7.pack(fill=tkinter.BOTH, expand=True)
        global employee_id_entry2
        employee_id_entry2 = Entry(black_screen7, width=40, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_id_entry2.pack(side=TOP)  
        global employee_id_button1
        employee_id_button1 = tkinter.Button(text="Enter the Employee Id to Search :", width=32, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_id_button1.place(x=520, y=291)
        continue_button = tkinter.Button(black_screen7, text='Continue',command=lambda: Record().search_id(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        continue_button.place(x=840, y=170)
        cancel_button = tkinter.Button(black_screen7, text='Cancel',command=lambda: Home().search_id_page(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        cancel_button.place(x=300, y=170)

    def search_name_window(self):
        black_screen6.destroy()
        home_button9.destroy()
        global employee_management_system3
        employee_management_system3 = tkinter.Label(text="", fg='white', bg='black', width=38, height=8, font=('TeX Gyre Adventor',20,"bold"))
        employee_management_system3.pack()
        global black_screen10
        black_screen10 = tkinter.Frame(height=1000, width=1000, bg='black')
        black_screen10.pack(fill=tkinter.BOTH, expand=True)
        global employee_name_entry2
        employee_name_entry2 = Entry(black_screen10, width=40, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_name_entry2.pack(side=TOP) 
        global employee_name_button1 
        employee_name_button1 = tkinter.Button(text="Enter the Employee Name to Search :", width=32, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_name_button1.place(x=520, y=291)
        continue_button = tkinter.Button(black_screen10, text='Continue',command=lambda: Record().search_name(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        continue_button.place(x=840, y=170)
        cancel_button = tkinter.Button(black_screen10, text='Cancel',command=lambda: Home().search_name_page(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        cancel_button.place(x=300, y=170)

    def search_age_window(self):
        black_screen6.destroy()
        home_button9.destroy()
        global employee_management_system4
        employee_management_system4 = tkinter.Label(text="", fg='white', bg='black', width=38, height=8, font=('TeX Gyre Adventor',20,"bold"))
        employee_management_system4.pack()
        global black_screen12
        black_screen12 = tkinter.Frame(height=1000, width=1000, bg='black')
        black_screen12.pack(fill=tkinter.BOTH, expand=True)
        global employee_age_entry2
        employee_age_entry2 = Entry(black_screen12, width=40, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_age_entry2.pack(side=TOP) 
        global employee_age_button1 
        employee_age_button1 = tkinter.Button(text="Enter the Employee Age to Search :", width=32, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_age_button1.place(x=520, y=291)
        continue_button = tkinter.Button(black_screen12, text='Continue',command=lambda: Record().search_age(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        continue_button.place(x=840, y=170)
        cancel_button = tkinter.Button(black_screen12, text='Cancel',command=lambda: Home().search_age_page(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        cancel_button.place(x=300, y=170)

    def search_salary_window(self):
        black_screen6.destroy()
        home_button9.destroy()
        global employee_management_system6
        employee_management_system6 = tkinter.Label(text="", fg='white', bg='black', width=38, height=8, font=('TeX Gyre Adventor',20,"bold"))
        employee_management_system6.pack()
        global black_screen14
        black_screen14 = tkinter.Frame(height=1000, width=1000, bg='black')
        black_screen14.pack(fill=tkinter.BOTH, expand=True)
        global employee_salary_entry2
        employee_salary_entry2 = Entry(black_screen14, width=40, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_salary_entry2.pack(side=TOP) 
        global employee_salary_button1 
        employee_salary_button1 = tkinter.Button(text="Enter the Employee Salary to Search :", width=38, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_salary_button1.place(x=520, y=291)
        continue_button = tkinter.Button(black_screen14, text='Continue',command=lambda: Record().search_salary(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        continue_button.place(x=840, y=170)
        cancel_button = tkinter.Button(black_screen14, text='Cancel',command=lambda: Home().search_salary_page(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        cancel_button.place(x=300, y=170)

    def search_increment_window(self):
        black_screen6.destroy()
        home_button9.destroy()
        global employee_management_system8
        employee_management_system8 = tkinter.Label(text="", fg='white', bg='black', width=38, height=8, font=('TeX Gyre Adventor',20,"bold"))
        employee_management_system8.pack()
        global black_screen16
        black_screen16 = tkinter.Frame(height=1000, width=1000, bg='black')
        black_screen16.pack(fill=tkinter.BOTH, expand=True)
        global employee_increment_entry2
        employee_increment_entry2 = Entry(black_screen16, width=40, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_increment_entry2.pack(side=TOP) 
        global employee_increment_button1 
        employee_increment_button1 = tkinter.Button(text="Enter the Employee Increment to Search :", width=38, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_increment_button1.place(x=520, y=291)
        continue_button = tkinter.Button(black_screen16, text='Continue',command=lambda: Record().search_increment(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        continue_button.place(x=840, y=170)
        cancel_button = tkinter.Button(black_screen16, text='Cancel',command=lambda: Home().search_increment_page(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        cancel_button.place(x=300, y=170)

    def search_mobile_no_window(self):
        black_screen6.destroy()
        home_button9.destroy()
        global employee_management_system10
        employee_management_system10 = tkinter.Label(text="", fg='white', bg='black', width=38, height=8, font=('TeX Gyre Adventor',20,"bold"))
        employee_management_system10.pack()
        global black_screen18
        black_screen18 = tkinter.Frame(height=1000, width=1000, bg='black')
        black_screen18.pack(fill=tkinter.BOTH, expand=True)
        global employee_mobile_no_entry2
        employee_mobile_no_entry2 = Entry(black_screen18, width=40, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_mobile_no_entry2.pack(side=TOP) 
        global employee_mobile_no_button1 
        employee_mobile_no_button1 = tkinter.Button(text="Enter the Employee Mobile No. to Search :", width=38, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_mobile_no_button1.place(x=520, y=291)
        continue_button = tkinter.Button(black_screen18, text='Continue',command=lambda: Record().search_mobile_no(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        continue_button.place(x=840, y=170)
        cancel_button = tkinter.Button(black_screen18, text='Cancel',command=lambda: Home().search_mobile_no_page(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        cancel_button.place(x=300, y=170)

    def update_window(self):
        global black_screen20
        black_screen20 = tkinter.Frame(height=1000, width=1000, bg='black')
        black_screen20.pack(fill=tkinter.BOTH, expand=True)
        global update_id_button
        update_id_button = Button(black_screen20, text="Update By Id",command=self.update_id_window, bg='#FFFACD', fg='black', width=24, height=2, font=('TeX Gyre Adventor',14,"normal"))
        update_id_button.place(x=500, y=125)
        global update_name_button
        update_name_button = Button(black_screen20, text="Update By Name",command=self.update_name_window ,bg='#FFFACD', fg='black', width=24, height=2, font=('TeX Gyre Adventor',14,"normal"))
        update_name_button.place(x=500, y=250)
        global home_button11
        home_button11 = tkinter.Button(text="Back", command=Home().update_page, bg='#FFFACD', fg='black', width=10, height=2, font=('TeX Gyre Adventor',14,"normal"))
        home_button11.place(x=1190, y=640) 
        

    def update_name_window(self):
        black_screen20.destroy()
        home_button11.destroy()
        global employee_management_system23
        employee_management_system23 = tkinter.Label(text="", fg='white', bg='black', width=38, height=8, font=('TeX Gyre Adventor',20,"bold"))
        employee_management_system23.pack()
        global black_screen25
        black_screen25 = tkinter.Frame(height=1000, width=1000, bg='black')
        black_screen25.pack(fill=tkinter.BOTH, expand=True)
        global employee_name_entry3
        employee_name_entry3 = Entry(black_screen25, width=40, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_name_entry3.pack(side=TOP)  
        global employee_name_button3
        employee_name_button3 = tkinter.Button(text="Enter the Employee Name to Update :", width=32, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_name_button3.place(x=520, y=291)
        continue_button = tkinter.Button(black_screen25, text='Continue',command=self.update_name_page, width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        continue_button.place(x=840, y=170)
        cancel_button = tkinter.Button(black_screen25, text='Cancel',command=lambda: Home().update_name_page(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        cancel_button.place(x=300, y=170)

    def update_id_window(self):
        black_screen20.destroy()
        home_button11.destroy()
        global employee_management_system21
        employee_management_system21 = tkinter.Label(text="", fg='white', bg='black', width=38, height=8, font=('TeX Gyre Adventor',20,"bold"))
        employee_management_system21.pack()
        global black_screen21
        black_screen21 = tkinter.Frame(height=1000, width=1000, bg='black')
        black_screen21.pack(fill=tkinter.BOTH, expand=True)
        global employee_id_entry3
        employee_id_entry3 = Entry(black_screen21, width=40, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_id_entry3.pack(side=TOP)  
        global employee_id_button3
        employee_id_button3 = tkinter.Button(text="Enter the Employee Id to Update :", width=32, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_id_button3.place(x=520, y=291)
        continue_button = tkinter.Button(black_screen21, text='Continue',command=self.update_id_page, width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        continue_button.place(x=840, y=170)
        cancel_button = tkinter.Button(black_screen21, text='Cancel',command=lambda: Home().update_id_page(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        cancel_button.place(x=300, y=170)
        
    def update_id_page(self):
        global black_screen22
        employee_id = employee_id_entry3.get()
        self.db_query("SELECT * FROM Records WHERE employee_id=?", [employee_id])
        if len(employee_id) == 0:
            enter_text1 = Label(black_screen21, text="Please Enter a Value !!! ", width=40, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text1.place(x=925, y=0)
            enter_text1.pack(side=RIGHT, align='UP', padx=200, pady=7)
            return
        elif len(data) == 0:
            emp_exist1 = Label(black_screen21, text="Employee Id doesn't Exist !!! ", width=40, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            emp_exist1.place(x=925, y=0)
            emp_exist1.pack(side=RIGHT, align='UP', padx=200, pady=7)
            return
        black_screen21.destroy()
        employee_management_system21.destroy()
        employee_id_button3.destroy()
        global black_screen26
        black_screen22 = tkinter.Frame(height=1000, width=1000, bg='black')
        black_screen22.pack(fill=tkinter.BOTH, expand=True)
        Record().default_name(employee_id)
        Record().default_age(employee_id)
        Record().default_salary(employee_id)
        Record().default_increment(employee_id)
        Record().default_experience(employee_id)
        Record().default_email_id(employee_id)
        Record().default_mobile_no(employee_id)
        employee_id_button = tkinter.Button(black_screen22, text="Employee Id", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_id_button.place(x=410, y=0)
        global employee_id_entry1
        employee_id_entry1 = Entry(black_screen22, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_id_entry1.insert(END, employee_id)
        employee_id_entry1.pack()  
        employee_name_button = tkinter.Button(black_screen22, text="Employee Name", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_name_button.place(x=410, y=37)
        global employee_name_entry1
        employee_name_entry1 = Entry(black_screen22, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_name_entry1.pack()
        employee_name_entry1.insert(END, default_employee_name)
        employee_age_button = tkinter.Button(black_screen22, text="Age", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_age_button.place(x=410, y=74)
        global employee_age_entry1
        employee_age_entry1 = Entry(black_screen22, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_age_entry1.pack()
        employee_age_entry1.insert(END, default_employee_age)
        employee_salary_button = tkinter.Button(black_screen22, text="Salary", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_salary_button.place(x=410, y=110)
        global employee_salary_entry1
        employee_salary_entry1 = Entry(black_screen22, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_salary_entry1.pack()
        employee_salary_entry1.insert(END, default_employee_salary)
        employee_increment_button = tkinter.Button(black_screen22, text="Increment", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_increment_button.place(x=410, y=147)
        global employee_increment_entry1
        employee_increment_entry1 = Entry(black_screen22, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_increment_entry1.pack()
        employee_increment_entry1.insert(END, default_employee_increment)
        employee_experience_button = tkinter.Button(black_screen22, text="Experience", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_experience_button.place(x=410, y=184)
        global employee_experience_entry1
        employee_experience_entry1 = Entry(black_screen22, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_experience_entry1.pack()
        employee_experience_entry1.insert(END, default_employee_experience)
        employee_email_id_button = tkinter.Button(black_screen22, text="Email Id", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_email_id_button.place(x=410, y=221)
        global employee_email_id_entry1
        employee_email_id_entry1 = Entry(black_screen22, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_email_id_entry1.pack()
        employee_email_id_entry1.insert(END, default_employee_email_id)
        employee_mobile_no_button = tkinter.Button(black_screen22, text="Mobile No.", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_mobile_no_button.place(x=410, y=258)
        global employee_mobile_no_entry1
        employee_mobile_no_entry1 = Entry(black_screen22, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_mobile_no_entry1.pack()
        employee_mobile_no_entry1.insert(END, default_employee_mobile_no)
        continue_button = tkinter.Button(black_screen22, text='Continue',command=lambda: Record().update_id(employee_id), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        continue_button.place(x=640, y=380)
        cancel_button = tkinter.Button(black_screen22, text='Cancel',command=lambda: Home().update_id_page1(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        cancel_button.place(x=430, y=380)

    def update_name_page(self):
        global black_screen26
        employee_name = employee_name_entry3.get()
        self.db_query("SELECT * FROM Records WHERE employee_name=?", [employee_name])
        if len(employee_name) == 0:
            enter_text1 = Label(black_screen25, text="Please Enter a Value !!! ", width=40, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            enter_text1.place(x=925, y=0)
            enter_text1.pack(side=RIGHT, align='UP', padx=200, pady=7)
            return
        elif len(data) == 0:
            emp_exist1 = Label(black_screen25, text="No Records Found for the Employee Name !!! ", width=40, bd=0, height=2, relief='flat', borderwidth=0, fg='red', bg='black', font=('TeX Gyre Adventor',14,"normal"))
            emp_exist1.place(x=925, y=0)
            emp_exist1.pack(side=RIGHT, align='UP', padx=200, pady=7)
            return
        black_screen25.destroy()
        employee_management_system23.destroy()
        employee_name_button3.destroy()
        black_screen26 = tkinter.Frame(height=1000, width=1000, bg='black')
        black_screen26.pack(fill=tkinter.BOTH, expand=True)
        Record().default_id1(employee_name)
        Record().default_age1(employee_name)
        Record().default_salary1(employee_name)
        Record().default_increment1(employee_name)
        Record().default_experience1(employee_name)
        Record().default_email_id1(employee_name)
        Record().default_mobile_no1(employee_name)
        employee_id_button = tkinter.Button(black_screen26, text="Employee Id", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_id_button.place(x=410, y=0)
        global employee_id_entry1
        employee_id_entry1 = Entry(black_screen26, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_id_entry1.insert(END, default_employee_id1)
        employee_id_entry1.pack()  
        employee_name_button = tkinter.Button(black_screen26, text="Employee Name", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_name_button.place(x=410, y=37)
        global employee_name_entry1
        employee_name_entry1 = Entry(black_screen26, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_name_entry1.pack()
        employee_name_entry1.insert(END, employee_name)
        employee_age_button = tkinter.Button(black_screen26, text="Age", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_age_button.place(x=410, y=74)
        global employee_age_entry1
        employee_age_entry1 = Entry(black_screen26, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_age_entry1.pack()
        employee_age_entry1.insert(END, default_employee_age1)
        employee_salary_button = tkinter.Button(black_screen26, text="Salary", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_salary_button.place(x=410, y=110)
        global employee_salary_entry1
        employee_salary_entry1 = Entry(black_screen26, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_salary_entry1.pack()
        employee_salary_entry1.insert(END, default_employee_salary1)
        employee_increment_button = tkinter.Button(black_screen26, text="Increment", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_increment_button.place(x=410, y=147)
        global employee_increment_entry1
        employee_increment_entry1 = Entry(black_screen26, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_increment_entry1.pack()
        employee_increment_entry1.insert(END, default_employee_increment1)
        employee_experience_button = tkinter.Button(black_screen26, text="Experience", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_experience_button.place(x=410, y=184)
        global employee_experience_entry1
        employee_experience_entry1 = Entry(black_screen26, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_experience_entry1.pack()
        employee_experience_entry1.insert(END, default_employee_experience1)
        employee_email_id_button = tkinter.Button(black_screen26, text="Email Id", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_email_id_button.place(x=410, y=221)
        global employee_email_id_entry1
        employee_email_id_entry1 = Entry(black_screen26, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_email_id_entry1.pack()
        employee_email_id_entry1.insert(END, default_employee_email_id1)
        employee_mobile_no_button = tkinter.Button(black_screen26, text="Mobile No.", width=14, height=0, fg='black', bg='#FFFACD', font=('Latin Modern Mono Slanted',13,'normal'))
        employee_mobile_no_button.place(x=410, y=258)
        global employee_mobile_no_entry1
        employee_mobile_no_entry1 = Entry(black_screen26, width=20, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',16,'normal'))
        employee_mobile_no_entry1.pack()
        employee_mobile_no_entry1.insert(END, default_employee_mobile_no1)
        continue_button = tkinter.Button(black_screen26, text='Continue',command=lambda: Record().update_name(employee_name), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        continue_button.place(x=640, y=380)
        cancel_button = tkinter.Button(black_screen22, text='Cancel',command=lambda: Home().update_name_page1(), width=14, height=1, bg='#FFFACD', fg='black', font=('Latin Modern Mono Slanted',12,'normal'))
        cancel_button.place(x=430, y=380)


if __name__ == '__main__':
    global employee_management_system
    employee_management_system = tkinter.Label(text="Employee Management System", fg='white', bg='black', width=30, height=4, font=('TeX Gyre Adventor',20,"bold"))
    employee_management_system.pack()
    create_a_table = tkinter.Button(window, text="Create Table", command=Record().create_table , bg='#FFFACD', fg='black', width=20, height=2, font=('TeX Gyre Adventor',14,"normal"))
    create_a_table.place(x=580, y=120)
    Home().patch()
    window.mainloop()












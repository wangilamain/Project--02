import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        # Patient info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            sex = sex_combobox.get()
            age = age_spinbox.get()
            race = race_combobox.get()
            
            # More Patient  info
            reg = reg_status_var.get()
            num = num_entry.get()
            numadd = numadd_entry.get()
            fac = fac_combobox.get()
            numb = numb_entry.get()
            # reg = reg_check.get()

            
            print("First name: ", firstname, "Last name: ", lastname, "Sex: ", sex,)
            print("Age: ", age, "Race: ", race, "Facility name: ", fac)
            print( "Medical record: ", num)
            print("Registration status", reg, "Phone number: ", numb, "Address: ", numadd)
            print("------------------------------------------")
            
            # Create Table
            conn = sqlite3.connect('records.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Patient_Data 
                    (firstname TEXT, lastname TEXT, sex TEXT, age INT, race TEXT, 
                    fac TEXT, num TEXT, reg TEXT,
                    numb INT, numadd TEXT)
            '''
            conn.execute(table_create_query)
            
            # Insert Data
            data_insert_query = '''INSERT INTO Patient_Data (firstname, lastname, sex, 
            age, race, fac, num, reg, numb, numadd) VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (firstname, lastname, sex, 
                                age, race, fac, num, reg, numb, numadd)
            cursor = conn.cursor()
            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()
            conn.close()

            
                
        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title(" Patient Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving Patient Info
patient_info_frame =tkinter.LabelFrame(frame, text="Patient Information")
patient_info_frame.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(patient_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(patient_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(patient_info_frame)
last_name_entry = tkinter.Entry(patient_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

sex_label = tkinter.Label(patient_info_frame, text="Sex")
sex_combobox = ttk.Combobox(patient_info_frame, values=["", "Male", "Female"])
sex_label.grid(row=0, column=2)
sex_combobox.grid(row=1, column=2)

age_label = tkinter.Label(patient_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(patient_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

race_label = tkinter.Label(patient_info_frame, text="Race")
race_combobox = ttk.Combobox(patient_info_frame, values=["Black", "White", "Asian/Pacific Islander", "Unknown", "Other"])
race_label.grid(row=2, column=1)
race_combobox.grid(row=3, column=1)

for widget in patient_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Facility Info
reg_frame = tkinter.LabelFrame(frame)
reg_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(reg_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(reg_frame, text="Out-patient",
                                       variable=reg_status_var, onvalue="Out-patient", offvalue="In-patient")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

num_label = tkinter.Label(reg_frame, text= " Medical record")
num_entry = tkinter.Entry(reg_frame)
num_label.grid(row=0, column=1)
num_entry.grid(row=1, column=1)




fac_label = tkinter.Label(patient_info_frame, text="Facility name")
fac_combobox = ttk.Combobox(patient_info_frame, values=["Nairobi South Hospital", "The Mater Hospital", "Kenyatta National Hospital", "Aga Khan Hospital ", "Avenue Hospital"])
fac_label.grid(row=2, column=2)
fac_combobox.grid(row=3, column=2)

numb_label = tkinter.Label(reg_frame, text= " Phone number")
numb_entry = tkinter.Entry(reg_frame)
numb_label.grid(row=0, column=2)
numb_entry.grid(row=1, column=2)

for widget in reg_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

numadd_label = tkinter.Label(reg_frame, text= " Address")
numadd_entry = tkinter.Entry(reg_frame)
numadd_label.grid(row=0, column=3)
numadd_entry.grid(row=1, column=3)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Save data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
 
window.mainloop()
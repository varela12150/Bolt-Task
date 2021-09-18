import tkinter as tk    #import tkinter
from tkinter import ttk
from csv import DictWriter
import os 
win = tk.Tk()
win.title('Bolt Foods Registration Account')    #give a title name

#create labels
#name label
name_label = ttk.Label(win,text = "Enter your Name: ")
name_label.grid(row=0, column=0, sticky = tk.W)

#email label
email_label = ttk.Label(win,text = "Enter Your Email: ")
email_label.grid(row=1, column = 0,sticky =tk.W)

#restaurant label
name_restaurant_label = ttk.Label(win,text = "Name restaurant: ")
name_restaurant_label.grid(row=2, column = 0, sticky = tk.W)

#mobile number label
mobile_label = ttk.Label(win, text = "Enter Your Mobile Number: ")
mobile_label.grid(row=3, column = 0, sticky =tk.W)

#address label
address_label = ttk.Label(win,text = "Select Your Address: ")
address_label.grid(row=4, column = 0, sticky = tk.W)

#gender label
gender_label = ttk.Label(win,text = "Select Your Gender: ")
gender_label.grid(row=5, column = 0, sticky = tk.W)

#payment_method  label
payment_method_label = ttk.Label(win,text = "Select Your payment_method: ")
payment_method_label.grid(row=6, column = 0, sticky = tk.W)

#Create entry box
#name entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width = 16, textvariable = name_var)
name_entrybox.grid(row=0 , column = 1)
name_entrybox.focus()

#email entry box
email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width = 16, textvariable = email_var)
email_entrybox.grid(row = 1, column = 1)

#restaurant entry box
restaurant_var = tk.StringVar()
restaurant_entrybox = ttk.Entry(win,width = 16, textvariable= restaurant_var)
restaurant_entrybox.grid(row=2, column =1)

#mobile entry box
mobile_var = tk.StringVar()
mobile_entrybox = ttk.Entry(win, width= 16, textvariable = mobile_var)
mobile_entrybox.grid(row=3, column= 1)

#address entry box
address_var = tk.StringVar()
address_entrybox = ttk.Entry(win, width= 16, textvariable = address_var)
address_entrybox.grid(row=4, column= 1)

#gender entry box
#create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win,width = 13, textvariable = gender_var, state="readonly")
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.current(0)
gender_combobox.grid(row = 5, column=1)

#payment_method entry box
payment_method_var = tk.StringVar()
payment_method_combobox = ttk.Combobox(win,width = 13, textvariable = payment_method_var, state="readonly")
payment_method_combobox['values'] = ('Credit_Card', 'Debit_Card', 'Cash')
payment_method_combobox.current(0)
payment_method_combobox.grid(row = 6, column=1)


#Create button code action function
def action():
    username = name_var.get()
    useremail = email_var.get()
    userrestaurant = restaurant_var.get()
    usermobile = mobile_var.get()
    useraddress = address_var.get()
    usergender = gender_var.get()
    userpaymentmethod = payment_method_var.get()

    #write to csv file code here
    with open('file.csv', 'a', newline = '') as f:
        dict_writer = DictWriter(f, fieldnames=['User Name', 'User Email', 'User Restaurant', 'User Mobile', 
                                                'User Address', 'User Gender', 'User payment method'])
        if os.stat('file.csv').st_size == 0:        #if file is not empty than header write else not
            dict_writer.writeheader()
       
        dict_writer.writerow({
            'User Name' : username,
            'User Email' : useremail,
            'User Restaurant': userrestaurant,
            'User Mobile' : usermobile,
            'User Address': useraddress,
            'User Gender' : usergender,
            'User payment method' : userpaymentmethod
        })

#Change color after submit button
    name_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    restaurant_entrybox.delete(0, tk.END)
    mobile_entrybox.delete(0, tk.END)
    address_entrybox.delete(0, tk.END)
    name_label.configure(foreground = 'Blue')
    email_label.configure(foreground = 'Blue')
    name_restaurant_label.configure(foreground = 'Blue')
    mobile_label.configure(foreground = 'Blue')
    address_label.configure(foreground = 'Blue')
    gender_label.configure(foreground = 'Blue')
    payment_method_label.configure(foreground = 'Blue')

#submit button
submit_button = ttk.Button(win, text = "Submit", command = action)  
submit_button.grid(row=7, column=0)
win.mainloop()      #application is not closed auto
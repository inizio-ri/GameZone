from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmpasswordEntry.delete(0, END)
    check.set(0)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmpasswordEntry.get=='':
        messagebox.showerror('Error','All fields are Required')
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error', 'Please accept Terms and Conditions')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Krishna@30')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error','Username Already Exists')

        else:
            query='insert into data(email, username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registeration is successful')
            clear()
            registeration_window.destroy()
            import Login


def login_page():
    registeration_window.destroy()
    import Login

registeration_window = Tk()
registeration_window.title('Registeration Page')
registeration_window.resizable(False,False)
background=ImageTk.PhotoImage(file='bg1.jpg')

bgLabel=Label(registeration_window, image=background)
bgLabel.grid()

frame=Frame(registeration_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text="CREATE AN ACCOUNT", font=('Cooper Black', 16, 'bold')
              ,bg='white',fg='VioletRed3')
heading.grid(row=0,column=0, padx=13,pady=12)



emailLabel=Label(frame,text='Email',font=('Times New Roman',12,'bold'),
                 bg='white',fg='VioletRed3')
emailLabel.grid(row=1,column=0,sticky='w',padx=25)

emailEntry=Entry(frame,width=30,font=('Times New Roman',12,'bold'),
                 fg='white',bg='VioletRed3')
emailEntry.grid(row=2,column=0,sticky='w',padx=25, pady=5)



usernameLabel=Label(frame,text='Username',font=('Times New Roman',12,'bold'),
                 bg='white',fg='VioletRed3')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25)

usernameEntry=Entry(frame,width=30,font=('Times New Roman',12,'bold'),
                 fg='white',bg='VioletRed3')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25,pady=5)



passwordLabel=Label(frame,text='Password',font=('Times New Roman',12,'bold'),
                 bg='white',fg='VioletRed3')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25)

passwordEntry=Entry(frame,width=30,font=('Times New Roman',12,'bold'),
                 fg='white',bg='VioletRed3')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25,pady=5)



confirmpasswordLabel=Label(frame,text='Confirm Password',font=('Times New Roman',12,'bold'),
                 bg='white',fg='VioletRed3')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25)

confirmpasswordEntry=Entry(frame,width=30,font=('Times New Roman',12,'bold'),
                 fg='white',bg='VioletRed3')
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=25,pady=5)
check=IntVar()
termsandconditions=Checkbutton(frame,text='I agree to the Terms and Conditions',font=('Times New Roman',10,'bold'),
                               fg='VioletRed3', bg='white', activebackground='white', activeforeground='VioletRed3',
                               cursor='hand2', variable=check)
termsandconditions.grid(row=9,column=0,sticky='w',padx=15,pady=10)

signupButton=Button(frame,text='Sign Up',font=('Times New Roman',16,'bold'),bd=0,bg='VioletRed3', fg='white',
                    activebackground='VioletRed3', activeforeground='white', width=17, command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount=Label(frame, text="Already have an account?", font=('Open Sans', 9,'bold'),
                    bg='white', fg='VioletRed3')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

loginButton=Button(frame, text='Login', font=('open Sans', 9, 'bold underline'),
                   bg='white', fg='blue', bd=0, cursor='hand2', activebackground='white',
                   activeforeground='blue', command=login_page)
loginButton.place(x=175,y=398)

registeration_window.mainloop()

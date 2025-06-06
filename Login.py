from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#Functionality Part
def forget_pass():
    window = Toplevel()
    window.title('Change Password')

    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bglabel=Label(window, image=bgPic)
    bglabel.grid()

    heading_label = Label(window, text='RESET PASSWORD', font=('Cooper Black',17,'bold'),
                          bg='white', fg='VioletRed3')
    heading_label.place(x=480,y=75)

    userLabel = Label(window, text='Username', font=('Times New Roman', 15,'bold'), bg='white', fg='VioletRed3')
    userLabel.place(x=470, y=145)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=200)


    password1Label = Label(window, text='Password', font=('Times New Roman', 14,'bold'), bg='white', fg='VioletRed3')
    password1Label.place(x=470, y=228)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=283)


    password2Label = Label(window, text=' Confirm Password', font=('Times New Roman', 14,'bold'), bg='white', fg='VioletRed3')
    password2Label.place(x=464, y=311)
    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=366)

    submitButton= Button(window, text='Submit', bd=0, bg='VioletRed3', fg='white', font=('Times New Roman', 16,'bold'),
                         width=20, cursor='hand2', activebackground='VioletRed3', activeforeground='white')
    submitButton.place(x=470, y=400)


    window.mainloop()

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Krishna@30')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established, Try Again.')
            return
    query = 'use userdata'
    mycursor.execute(query)
    query='select * from data where username=%s and password=%s'
    mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
    row=mycursor.fetchone()
    if row==None:
        messagebox.showerror('Error','Invalid Username and Password')
    else:
        #messagebox.showinfo('Welcome','Login is successful')
        login_window.destroy()
        import Dashboard


def registeration_page():
    login_window.destroy()
    import Registeration

def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get()=='Username':
      usernameEntry.delete(0,END)

def pass_enter(event):
    if passwordEntry.get()=='Password':
      passwordEntry.delete(0,END)

#GUI Part
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Welcome to Gamezone')
bgImage = ImageTk.PhotoImage(file='bg1.jpg')

bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text="USER LOGIN", font=('Cooper Black', 23, 'bold')
              ,bg='white',fg='VioletRed3')
heading.place(x=605,y=120)

usernameEntry = Entry(login_window,width=25,font=('Times New Roman', 11, 'bold')
                    ,bd=0,fg='VioletRed3')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

frame1 = Frame(login_window,width=250,height=2,bg='VioletRed3')
frame1.place(x=580,y=222)

passwordEntry = Entry(login_window,width=25,font=('Times New Roman', 11, 'bold')
                    ,bd=0,fg='VioletRed3')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',pass_enter)

frame2 = Frame(login_window,width=250,height=2,bg='VioletRed3')
frame2.place(x=580,y=282)
openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white', activebackground='white'
                 ,cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

forgetButton=Button(login_window,text='Forget Password?',bd=0,bg='white', activebackground='white'
                 ,cursor='hand2', font=('Times New Roman', 11, 'bold'),
                    fg='VioletRed3', activeforeground='VioletRed3', command=forget_pass)
forgetButton.place(x=715,y=295)

loginButton=Button(login_window, text= 'Login', font=('open Sans',16,'bold'),
                   fg='white',bg='VioletRed3',activeforeground='white',
                   activebackground='VioletRed3',cursor='hand2',bd=0,width=19, command= login_user)
loginButton.place(x=578,y=350)

orLabel=Label(login_window,text='--------------OR--------------',font=('Open Sans', 16),fg='VioletRed3',bg='white')
orLabel.place(x=590,y=400)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=630,y=440)

google_logo=PhotoImage(file='google.png')
gLabel=Label(login_window,image=google_logo,bg='white')
gLabel.place(x=690,y=440)

twitter_logo=PhotoImage(file='twitter.png')
tLabel=Label(login_window,image=twitter_logo,bg='white')
tLabel.place(x=750,y=440)

registerLabel=Label(login_window,text='Dont have an account?',font=('Open Sans', 9,'bold'),fg='VioletRed3',bg='white')
registerLabel.place(x=590,y=500)

newaccountButton=Button(login_window, text= 'Create new one', font=('open Sans',9,'bold underline'),
                   fg='blue',bg='white',activeforeground='blue',
                   activebackground='white',cursor='hand2',bd=0, command=registeration_page)
newaccountButton.place(x=727,y=500)

login_window.mainloop()
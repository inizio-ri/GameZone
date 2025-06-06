from tkinter import *
from PIL import ImageTk

def play1_page():
    user_window.destroy()
    import Game1

def play2_page():
    user_window.destroy()
    import Game2

def play3_page():
    user_window.destroy()
    import Game3


user_window = Tk()
user_window.title('Dashboard')
user_window.resizable(False,False)

background = ImageTk.PhotoImage(file='bg1.jpg')

bgLabel=Label(user_window, image=background)
bgLabel.grid()

frame=Frame(user_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text="Choose any Game", font=('Cooper Black', 21, 'bold')
              ,bg='white',fg='VioletRed3')
heading.grid(row=0,column=0, padx=13,pady=13)



game1Button=Button(frame,text='Space Invaders', font=('Times New Roman',19,'bold'),bd=0,bg='VioletRed3',fg='white',
                   activebackground='VioletRed3',activeforeground='white', width= 18, height=2, command=play1_page)
game1Button.grid(row=1, column=0, padx=12,pady=12)



game2Button=Button(frame,text='Pong', font=('Times New Roman',19,'bold'),bd=0,bg='VioletRed3',fg='white',
                   activebackground='VioletRed3',activeforeground='white', width= 18, height=2, command=play2_page)
game2Button.grid(row=2, column=0, padx=12,pady=12)



game3Button=Button(frame,text='Tetris', font=('Times New Roman',19,'bold'),bd=0,bg='VioletRed3',fg='white',
                   activebackground='VioletRed3',activeforeground='white', width= 18, height=2, command=play3_page)
game3Button.grid(row=3, column=0, padx=12,pady=12)



wish=Label(frame,text="Best of Luck!!", font=('Times New Roman', 15, 'bold')
              ,bg='white',fg='VioletRed3')
wish.grid(row=4,column=0, padx=13,pady=13)

user_window.mainloop()
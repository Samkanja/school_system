from tkinter import *
from PIL import ImageTk

window = Tk()

window.geometry('1280x700+0+0')


window.resizable(False,False)


background_image = ImageTk.PhotoImage(file='logo/drive-download-20230324T003849Z-001/bg.jpg')


background_label = Label(window,image=background_image)


background_label.place(x=0,y=0)

login_frame = Frame(window,bg='white')

login_frame.place(x=400,y=150)

logo_image = PhotoImage(file='logo/drive-download-20230324T003849Z-001/student.png')

logo_label = Label(login_frame,image=logo_image)

logo_label.grid(row=0,column=0,columnspan=2)

username_image = PhotoImage(file='logo/drive-download-20230324T003849Z-001/user.png')

username_label = Label(login_frame,image=username_image,text='Username',compound=LEFT,
                       font=('times new roman',20,'bold'))


username_label.grid(row=1,column=0)

username_entry = Entry(login_frame)

username_entry.grid(row=1,column=1)




window.mainloop()
from tkinter import *


root = Tk() 
menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 


Label(root, text='First Name').grid(row=0) 
Label(root, text='Last Name').grid(row=1) 
e1 = Entry(root) 
e2 = Entry(root) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1)



mainloop()




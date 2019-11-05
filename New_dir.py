from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
import os

def get_name():
    folder_name=simpledialog.askstring(" Folder nameing time ", " please enter name of folder.")
    # py_file_name=simpledialog.askstring(" Py Folder name ", " please enter name of folder.")
    try: 
        os.chdir("c:/Users/JimRB/Desktop/")
        os.mkdir(folder_name)     
        os.chdir('c:/Users/JimRB/Desktop/'+folder_name)
        os.mkdir('venv')
        f = open('.gitignore','w+')
        # os.chdir('c:/Users/JimRB/Desktop/'+folder_name + '/.gitignore')
        # f = write("testicle")
        f.close()
        
 
        # f = open(input(py_file_name)+'.py','w')
    except OSError:
        messagebox.showinfo('','SOMETHING WENT WRONG!!!!')
        button1.quit()
    else:
        messagebox.showinfo('GUESS WHAT','Folder was succesfully created')
      
        
        button1.quit()


root =Tk()
button1 = Button(root, text='You want to create a folder? ', command=get_name)
button1.pack()

root.geometry('300x100')  #width x height of window

root.mainloop()

# name = messagebox.input(f' What do you want to call this folder =====>>>>   ')
# subfolder =  input(f' What do you want to call this subfolder?? =====>>>>   ')


from tkinter import *
from tkinter import filedialog


def neoask():
    def browseFilesA():
        s = filedialog.askopenfilename(initialdir="/",
                                       title="Select a File",
                                       filetypes=(("Python file",
                                                   "*.py*"),
                                                  ("all files",
                                                   "*.*")))

        f = open(s, "r")
        string = f.read()
        f.close()
        f = open("bot_A.py", "w")
        f.write(string)
        f.close()

        label_file_explorer.configure(text="File Opened: " + s)

    def browseFilesB():
        s = filedialog.askopenfilename(initialdir="/",
                                       title="Select a File",
                                       filetypes=(("Python file",
                                                   "*.py*"),
                                                  ("all files",
                                                   "*.*")))
        f = open(s, "r")
        string = f.read()
        f.close()
        f = open("bot_B.py", "w")
        f.write(string)
        f.close()

        label_file_explorer.configure(text="File Opened: " + s)


    window = Tk()
    window.title('File Explorer')
    window.geometry("350x200")
    window.config(background="white")
    label_file_explorer = Label(window,
                                text="Select Files:",
                                width=50, height=4,
                                fg="blue")
    button_explore_A = Button(window,
                            text="Bot A (Browse)",
                            command=browseFilesA, width=10)
    button_explore_B = Button(window,
                              text="Bot B (Browse)",
                              command=browseFilesB, width=10)
    button_exit = Button(window,
                         text="Exit",
                         command=window.destroy, width=10)
    window.grid_columnconfigure(2)
    label_file_explorer.grid(column=1, row=1)
    button_explore_A.grid(column=1, row=2)
    button_explore_B.grid(column=1, row=3)
    button_exit.grid(column=1, row=4)
    window.mainloop()













def ask():
    s = input() + '.py'
    try:
        f = open(s, "r")
        str = f.read()
        f.close()
        f = open("bot_A.py", "w")
        f.write(str)
        f.close()
        f = open(s, "r")
        str = f.read()
        f.close()
        f = open("bot_B.py", "w")
        f.write(str)
        f.close()
        return 0
    except:
        return 1

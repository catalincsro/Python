from tkinter import *

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=self.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def quit(self):
        root.destroy()

root = Tk()
my_gui = MyFirstGUI(master=root)
root.mainloop()

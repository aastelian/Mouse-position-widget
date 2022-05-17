import mouse
import tkinter as tk


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("250x200")
        self.root.title("Mouse Position on Screen")
        self.posLabel = tk.Label(self.root,text=f"""Mouse position on Screen:
        mouse.get_position()""")
        self.posLabel.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        self.find_position()

        self.root.mainloop()

    def find_position(self):
        self.posLabel.config(text=f"""Mouse position on Screen:
{mouse.get_position()[0]},{mouse.get_position()[1]}""")
        self.root.after(10,self.find_position)

App()
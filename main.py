from tkinter import *
from tkinter import ttk
from data_base import DataBase
from view import View

FILE_PATH = "database.json"

if __name__ == "__main__":
    print("rodando")
    root = Tk()
    view = View(root)
    view.renderHome()
    root.mainloop()

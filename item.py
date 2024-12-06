from tkinter import messagebox


class Item:

    def verifyItem(func):
        def wrapper(name, description, quantity):
            if len(name) == 0:
                return messagebox.showerror("Erro", "Nome inválido")
            elif quantity < 1:
                return messagebox.showerror("Erro", "Quantidade inválida")
            else:
                return func(name, description, quantity)

        return wrapper

    @verifyItem
    def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity

        self.__saveItem()

    def __saveItem(self):
        pass

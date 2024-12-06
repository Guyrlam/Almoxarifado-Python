from tkinter import messagebox


class User:

    def verifyUser(func):
        def wrapper(name, description, quantity):
            if len(name) == 0:
                return messagebox.showerror("Erro", "Nome inválido")
            elif quantity < 1:
                return messagebox.showerror("Erro", "Quantidade inválida")
            else:
                return func(name, description, quantity)

        return wrapper

    @verifyUser
    def __init__(self, name, password):
        self.name = name
        self.password = password

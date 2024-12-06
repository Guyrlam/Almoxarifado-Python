from tkinter import *
from tkinter import ttk

lista = [
    [1, "Joao Futi Muanda", "joao@mail.com", "12", ">"],
    [2, "Fortnato Mpngo", "joao@mail.com", 12, ">"],
    [3, "Usando Python", "joao@mail.com", 12, ">"],
    [4, "Clinton Berclidio", "joao@mail.com", 12, ">"],
    [5, "A traicao da Julieta", "joao@mail.com", 12, ">"],
]

listaUsers = [
    {
        "id": 0,
        "name": "Jorge",
        "password": "1234",
        "products": [
            [1, "Joao Futi Muanda", "joao@mail.com", "12", ">"],
            [2, "Fortnato Mpngo", "joao@mail.com", 12, ">"],
            [3, "Usando Python", "joao@mail.com", 12, ">"],
            [4, "Clinton Berclidio", "joao@mail.com", 12, ">"],
            [5, "A traicao da Julieta", "joao@mail.com", 12, ">"],
        ],
    },
    {
        "id": 1,
        "name": "Ana",
        "password": "abcd",
        "products": [
            [1, "Joao Futi Muanda", "joao@mail.com", "12", ">"],
            [2, "Fortnato Mpngo", "joao@mail.com", 12, ">"],
            [3, "Usando Python", "joao@mail.com", 12, ">"],
            [4, "Clinton Berclidio", "joao@mail.com", 12, ">"],
            [5, "A traicao da Julieta", "joao@mail.com", 12, ">"],
        ],
    },
    {
        "id": 2,
        "name": "Carlos",
        "password": "qwerty",
        "products": [
            [1, "Joao Futi Muanda", "joao@mail.com", "12", ">"],
            [2, "Fortnato Mpngo", "joao@mail.com", 12, ">"],
            [3, "Usando Python", "joao@mail.com", 12, ">"],
            [4, "Clinton Berclidio", "joao@mail.com", 12, ">"],
            [5, "A traicao da Julieta", "joao@mail.com", 12, ">"],
        ],
    },
]


black = "#00000f"
white = "#feffff"
green = "#4fa882"
darkBlue = "#38576b"
blue = "#038cfc"
red = "#ef5350"
darkGreen = "#263238"
lightBlue = "#e9edf5"
darkOrange = "#ff8c00"


class View:

    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de estoque")
        self.root.geometry("1043x453")
        self.root.configure(background=white)
        self.root.resizable(width=False, height=False)
        # self.root.protocol("WM_DELETE_WINDOW", onClose)

    def renderHome(self):
        for child in self.root.winfo_children():
            child.destroy()

        homeHeader = Frame(self.root, width=770, height=50, bg=darkOrange, relief="flat")
        homeHeader.grid(row=0, column=0)

        homeNav = Frame(self.root, width=273, height=50, bg=darkOrange, relief="flat")
        homeNav.grid(row=0, column=1)

        homeSearch = Frame(self.root, width=1043, height=50, bg=darkOrange, relief="solid")
        homeSearch.grid(row=1, column=0, columnspan=2)

        homeMain = Frame(self.root, width=1043, height=353, bg=white, relief="flat")
        homeMain.grid(row=2, column=0, columnspan=2, sticky="nsew")

        # Configurando o grid para expandir o homeMain
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        headerLabel = Label(
            homeHeader,
            text="Gerenciador de estoque",
            font="Roboto 13 bold",
            bg=darkOrange,
            fg=white,
            relief="flat",
        )
        headerLabel.place(x=10, y=10)

        editClientButton = Button(
            homeNav,
            text="Editar usuário",
            width=15,
            font="Roboto 8 bold",
            bg=white,
            fg=black,
            relief="raised",
            overrelief="ridge",
            command=self.renderEditUserForm
        )
        editClientButton.place(x=0, y=15)

        createProductButton = Button(
            homeNav,
            text="Novo produto",
            width=15,
            font="Roboto 8 bold",
            bg=white,
            fg=black,
            relief="raised",
            overrelief="ridge",
            command=self.renderProductForm,
        )
        createProductButton.place(x=135, y=15)

        tabela_head = ["ID", "Nome", "Descrição", "Quantidade", ""]

        tree = ttk.Treeview(
            homeMain, selectmode="extended", columns=tabela_head, show="headings"
        )

        vsb = ttk.Scrollbar(homeMain, orient="vertical", command=tree.yview)

        tree.configure(yscrollcommand=vsb.set)
        tree.grid(column=0, row=0, sticky="nsew")
        vsb.grid(column=1, row=0, sticky="ns")

        def abrir_modal(*args):
            item_id = tree.focus()
            self.renderEditProductForm(int(item_id))

        # Configurando o grid para expandir a tabela dentro de homeMain
        homeMain.grid_rowconfigure(0, weight=1)
        homeMain.grid_columnconfigure(0, weight=1)

        hd = [
            "nw",
            "nw",
            "nw",
            "center",
            "ne",
        ]
        h = [40, 280, 480, 100, 5]
        n = 0

        for col in tabela_head:
            tree.heading(col, text=col.title(), anchor=CENTER)
            tree.column(col, width=h[n], anchor=hd[n])
            n += 1

        for index, item in enumerate(lista):
            if index % 2 == 0:
                tree.insert("", "end", values=item, tags=("even",), iid=index)
            else:
                tree.insert("", "end", values=item, tags=("odd",), iid=index)

        tree.bind("<<TreeviewSelect>>", abrir_modal)

        # Configurando as cores para as tags
        tree.tag_configure("even", background="#f2f2f2")  # Cor de fundo clara
        tree.tag_configure("odd", background="#ffffff")

    def renderProductForm(self, *args):
        for child in self.root.winfo_children():
            child.destroy()

        # Cabeçalho do formulário
        formHeader = Frame(self.root, width=1043, height=50, bg="green", relief="flat")
        formHeader.grid(row=0, column=0)
        formHeader.pack_propagate(False)

        headerLabel = Label(
            formHeader,
            text="Criação de Produto",
            font="Roboto 13 bold",
            bg="green",
            fg="white",
            relief="flat",
        )
        headerLabel.pack(expand=True)

        # Corpo principal do formulário
        formMain = Frame(self.root, width=1043, height=403, bg="white", relief="flat")
        formMain.grid(row=1, column=0, sticky="nsew", pady=(0, 20), padx=40)
        formMain.grid_propagate(False)

        # Campo para Nome
        Label(formMain, text="Nome:", font="Roboto 8 bold", bg="white").grid(
            row=0, column=0, sticky="w", pady=15
        )
        nome_entry = Entry(
            formMain,
            textvariable=StringVar(),
            font="Roboto 8 bold",
            width=50,
            relief="solid",
        )
        nome_entry.grid(row=0, column=1, pady=5, padx=10, sticky="w")

        # Campo para Descrição (caixa de texto maior)
        Label(formMain, text="Descrição:", font="Roboto 8 bold", bg="white").grid(
            row=1, column=0, sticky="nw", pady=15
        )
        descricao_text = Text(
            formMain, font="Roboto 8 bold", width=50, height=10, relief="solid"
        )
        descricao_text.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        # Campo para Contador (Spinbox)
        Label(formMain, text="Quantidade:", font="Roboto 8 bold", bg="white").grid(
            row=2, column=0, sticky="w", pady=15
        )
        quantidade_spin = Spinbox(
            formMain, from_=0, to=100, font="Roboto 8 bold", width=10, relief="solid"
        )
        quantidade_spin.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        # Botão de Enviar
        def submit_form():
            nome = nome_entry.get()
            descricao = descricao_text.get("1.0", "end").strip()
            quantidade = quantidade_spin.get()
            print(f"Nome: {nome}, Descrição: {descricao}, Quantidade: {quantidade}")

        buttonsFrame =  Frame(formMain, bg="white", relief="flat")
        buttonsFrame.grid(row=3, column=0, pady=20, padx=40, columnspan=2)

        return_button = Button(
            buttonsFrame,
            text="Voltar",
            font="Roboto 8 bold",
            bg="black",
            fg="white",
            width=15,
            command=self.renderHome,
            relief="raised",
            overrelief="ridge",
        )
        return_button.grid(row=0, column=0, pady=20, padx=4)
        
        submit_button = Button(
            buttonsFrame,
            text="Continuar",
            font="Roboto 8 bold",
            bg="green",
            fg="white",
            width=15,
            command=submit_form,
            relief="raised",
            overrelief="ridge",
        )
        submit_button.grid(row=0, column=2, pady=20, padx=4)
        
        delete_button = Button(
            buttonsFrame,
            text="Deletar",
            font="Roboto 8 bold",
            bg="red",
            fg="white",
            width=15,
            command=submit_form,
            relief="raised",
            overrelief="ridge",
        )
        delete_button.grid(row=0, column=3, pady=20, padx=4)

    def renderEditProductForm(self,id):
        # Limpar a janela principal
        for child in self.root.winfo_children():
            child.destroy()

        # Cabeçalho do formulário
        formHeader = Frame(self.root, width=1043, height=50, bg="green", relief="flat")
        formHeader.grid(row=0, column=0)
        formHeader.pack_propagate(False)

        headerLabel = Label(
            formHeader,
            text="Criação de Produto",
            font="Roboto 13 bold",
            bg="green",
            fg="white",
            relief="flat",
        )
        headerLabel.pack(expand=True)

        # Corpo principal do formulário
        formMain = Frame(self.root, width=1043, height=403, bg="white", relief="flat")
        formMain.grid(row=1, column=0, sticky="nsew", pady=(0, 20), padx=40)
        formMain.grid_propagate(False)

        # Campo para Nome
        Label(formMain, text="Nome:", font="Roboto 8 bold", bg="white").grid(
            row=0, column=0, sticky="w", pady=15
        )
        nome_entry = Entry(
            formMain,
            textvariable=StringVar(),
            font="Roboto 8 bold",
            width=50,
            relief="solid",
        )
        nome_entry.grid(row=0, column=1, pady=5, padx=10, sticky="w")

        # Campo para Descrição (caixa de texto maior)
        Label(formMain, text="Descrição:", font="Roboto 8 bold", bg="white").grid(
            row=1, column=0, sticky="nw", pady=15
        )
        descricao_text = Text(
            formMain, font="Roboto 8 bold", width=50, height=10, relief="solid"
        )
        descricao_text.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        # Campo para Contador (Spinbox)
        Label(formMain, text="Quantidade:", font="Roboto 8 bold", bg="white").grid(
            row=2, column=0, sticky="w", pady=15
        )
        quantidade_spin = Spinbox(
            formMain, from_=0, to=100, font="Roboto 8 bold", width=10, relief="solid"
        )
        quantidade_spin.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        nome_entry.insert(0, lista[id][1])
        descricao_text.insert("1.0", lista[id][2])
        quantidade_spin.delete(0, "end")
        quantidade_spin.insert(0, lista[id][3])

        # Botão de Enviar
        def submit_form():
            nome = nome_entry.get()
            descricao = descricao_text.get("1.0", "end").strip()
            quantidade = quantidade_spin.get()
            print(f"Nome: {nome}, Descrição: {descricao}, Quantidade: {quantidade}")

        buttonsFrame =  Frame(formMain, bg="white", relief="flat")
        buttonsFrame.grid(row=3, column=0, pady=20, padx=40, columnspan=2)

        return_button = Button(
            buttonsFrame,
            text="Voltar",
            font="Roboto 8 bold",
            bg="black",
            fg="white",
            width=15,
            relief="raised",
            overrelief="ridge",
            command=self.renderHome,
        )
        return_button.grid(row=0, column=0, pady=20, padx=4)
        
        submit_button = Button(
            buttonsFrame,
            text="Continuar",
            font="Roboto 8 bold",
            bg="green",
            fg="white",
            width=15,
            command=submit_form,
            relief="raised",
            overrelief="ridge",
        )
        submit_button.grid(row=0, column=2, pady=20, padx=4)
        
        delete_button = Button(
            buttonsFrame,
            text="Deletar",
            font="Roboto 8 bold",
            bg="red",
            fg="white",
            width=15,
            command=submit_form,
            relief="raised",
            overrelief="ridge",
        )
        delete_button.grid(row=0, column=3, pady=20, padx=4)

    def renderEditUserForm(self, id=1):
        # Limpar a janela principal
        for child in self.root.winfo_children():
            child.destroy()

        # Cabeçalho do formulário
        formHeader = Frame(self.root, width=1043, height=50, bg=darkBlue, relief="flat")
        formHeader.grid(row=0, column=0)
        formHeader.pack_propagate(False)

        headerLabel = Label(
            formHeader,
            text="Editar usuário",
            font="Roboto 13 bold",
            bg=darkBlue,
            fg="white",
            relief="flat",
        )
        headerLabel.pack(expand =True)

        # Corpo principal do formulário
        formMain = Frame(self.root, width=1043, height=403, bg="white", relief="flat")
        formMain.grid(row=1, column=0, sticky="nsew", pady=(20, 40))
        formMain.grid_propagate(False)

        # Campo para Nome
        Label(formMain, text="Nome:", font="Roboto 8 bold", bg="white").grid(
            row=0, column=0, sticky="w", pady=15, padx=(40, 0)
        )
        nome_entry = Entry(
            formMain,
            textvariable=StringVar(),
            font="Roboto 8 bold",
            width=50,
            relief="solid",
        )
        nome_entry.grid(row=0, column=1, pady=5, padx=10, sticky="w")

        # Campo para Nome
        Label(formMain, text="Senha:", font="Roboto 8 bold", bg="white").grid(
            row=1, column=0, sticky="w", pady=15, padx=(40, 0)
        )
        password_entry = Entry(
            formMain,
            textvariable=StringVar(),
            font="Roboto 8 bold",
            width=50,
            relief="solid",
        )
        password_entry.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        nome_entry.insert(0, listaUsers[id]["name"])
        password_entry.insert(0, listaUsers[id]["password"])

        # Botão de Enviar
        def submit_form():
            nome = nome_entry.get()
            senha = password_entry.get()
            print(f"Nome: {nome}, Descrição: {nome}, Quantidade: {senha}")
            
        buttonsFrame =  Frame(formMain, bg="white", relief="flat")
        buttonsFrame.grid(row=3, column=0, pady=20, padx=40, columnspan=2)

        submit_button = Button(
            buttonsFrame,
            text="Voltar",
            font="Roboto 8 bold",
            bg="black",
            fg="white",
            width=15,
            command=self.renderHome,
            relief="raised",
            overrelief="ridge",
        )
        submit_button.grid(row=0, column=0, pady=20, padx=4)
        
        return_button = Button(
            buttonsFrame,
            text="Continuar",
            font="Roboto 8 bold",
            bg="green",
            fg="white",
            width=15,
            command=submit_form,
            relief="raised",
            overrelief="ridge",
        )
        return_button.grid(row=0, column=2, pady=20, padx=4)
        
        delete_button = Button(
            buttonsFrame,
            text="Deletar",
            font="Roboto 8 bold",
            bg="red",
            fg="white",
            width=15,
            command=submit_form,
            relief="raised",
            overrelief="ridge",
        )
        delete_button.grid(row=0, column=3, pady=20, padx=4)

    def createLoginForm(self):
        # Limpar a janela principal
        for child in self.root.winfo_children():
            child.destroy()

        formHeader = Frame(self.root, width=1043, height=50, bg=darkBlue, relief="flat")
        formHeader.grid(row=0, column=0)
        formHeader.pack_propagate(False)

        headerLabel = Label(
            formHeader,
            text="Editar usuário",
            font="Roboto 13 bold",
            bg=darkBlue,
            fg="white",
            relief="flat",
        )
        headerLabel.pack(expand=True)

        # Corpo principal do formulário
        formMain = Frame(self.root, width=1043, height=403, bg="white", relief="flat")
        formMain.grid(row=1, column=0, sticky="nsew", pady=(20, 40))
        formMain.grid_propagate(False)

        # Campo para Nome
        Label(formMain, text="Nome:", font="Roboto 8 bold", bg="white").grid(
            row=0, column=0, sticky="w", pady=15, padx=(40, 0)
        )
        nome_entry = Entry(
            formMain,
            textvariable=StringVar(),
            font="Roboto 8 bold",
            width=50,
            relief="solid",
        )
        nome_entry.grid(row=0, column=1, pady=5, padx=10, sticky="w")

        # Campo para Nome
        Label(formMain, text="Senha:", font="Roboto 8 bold", bg="white").grid(
            row=1, column=0, sticky="w", pady=15, padx=(40, 0)
        )
        password_entry = Entry(
            formMain,
            textvariable=StringVar(),
            font="Roboto 8 bold",
            width=50,
            relief="solid",
        )
        password_entry.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        # Botão de Enviar
        def submit_form():
            nome = nome_entry.get()
            senha = password_entry.get()
            print(f"Nome: {nome}, Descrição: {nome}, Quantidade: {senha}")

        submit_button = Button(
            formMain,
            text="Continuar",
            font="Roboto 8 bold",
            bg="green",
            fg="white",
            width=15,
            command=submit_form,
            relief="raised",
            overrelief="ridge",
        )
        submit_button.grid(row=3, column=1, pady=20, columnspan=2)

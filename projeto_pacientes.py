from tkinter import *
from tkinter import ttk 
from tkinter import messagebox 

#Janela principal 
janela = Tk ()
janela.title("Cadastro para pacientes")
janela.geometry("700x400")

abas = ttk.Notebook(janela)
abas.pack(fill="both", expand=True)
#aba1 - Cadastro 
aba1= Frame(abas)
abas.add(aba1, text = "Cadastro")

#abas2 - Tabela
aba2= Frame(abas)
abas.add(aba2, text = "Pacientes cadastrados")

#Função cadastrar 
def cadastrar ():
    Nome = entry_Nome.get()
    CPF =  entry_CPF.get()
    Data_de_Nascimento = entry_Data_de_Nascimento.get()
    Telefone = entry_Telefone.get()
    Email = entry_Email.get()
    Convênio/SUS =entry_Convênio/SUS.get()
    Contato_de_emergência =entry_Contato_de_emergência.get()

    if Nome == "" or CPF == "" or Data_de_Nascimento == "" or  Telefone == "" or Email == "" or Convênio/SUS == "" or Contato_de_emergência == "":
        messagebox.showwarning ("Erro!", "Preencha todos os campos!")
    else: 
        tabela.insert("", END, values =(Nome, CPF, Data_de_Nascimento,Telefone,Email, Convênio/SUS, Contato_de_emergência ))
        entry_Nome.delete(0, END)
        entry_CPF.delete(0, END)
        entry_Data_de_Nascimento.delete(0, END)
        entry_Telefone.delete(0,END)
        entry_Email.delete(0,END)
        entry_Convênio/SUS.delete(0,END)
        entry_Contato_de_Emergência.delete(0, END)

        Message.box.showinfo("Sucesso", "Cliente cadastrado!")

###Aba Cadastro 
Label(aba1, text= "Nome").pack(pady=5)
entry_Nome = Entry(aba1, width=40)
entry_nome.pack()

Label(aba1, text= "CPF").pack(pady=5)
entry_CPF = Entry(aba1, width=40)
entry_CPF.pack()

Label(aba1, text= "Data_de_Nascimento").pack(pady=5)
entry_Data_de_Nascimento = Entry(aba1, width=40)
entry_Data_de_Nascimento.pack()

Label(aba1, text= "Telefone").pack(pady=5)
entry_Telefone = Entry(aba1, width=40)
entry_Telefone.pack()

Label(aba1, text= "Email").pack(pady=5)
entry_Email = Entry(aba1, width=40)
entry_Email.pack()


Label(aba1, text= "Convênio/SUS").pack(pady=5)
entry_Convênio/SUS= Entry(aba1, width=40)
entry_Convênio/SUS.pack()

Label(aba1, text= "Contato_de_Emergência").pack(pady=5)
entry_Contato_de_Emergência= Entry(aba1, width=40)
entry_Contato_de_Emergência.pack()

Button(
    aba1, 
    text= "Cadastrar",
    bg="black",
    fg="white",
    width=20,
    command=cadastrar
).pack(pady=20)



###aba Tabela
colunas = ("Nome", "CPF", "Data_de_Nascimento", "Telefone", "Email", "Convênio/SUS", "entry_Contato_de_Emergência")
tabela =ttk.Treeview(
    aba2,
    columns= colunas
    show="headings"
)
for col  in colunas:
    tabela.heading(col,text=col)
    tabela.column(col, width=150)

    tabela.pack(fill="both",expand=True, pady=20)

    janela.mainloop()




    
    
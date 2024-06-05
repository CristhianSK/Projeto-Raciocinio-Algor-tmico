import customtkinter
import sqlite3
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title("login")
app.geometry("450x360")
app.config(bg="#001220")

font1 = ("Helvetica", 25, "bold")
font2 = ("Arial", 17, "bold")
font3 = ("Arial", 13, "bold")
font4 = ("Arial", 13, "bold", "underline")

conn = sqlite3.connect("data2.db")
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios(
               usuario TEXT NOT NULL,
               senha TEXT NOT NULL
               funcionario CHECKBOX NOT NULL)""")

def checkbox_event():
    print("checkbox toggled, current value:", funcionario.get())


def cadastro():
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    if usuario != "" and senha != "":
        cursor.execute("SELECT usuario FROM usuarios WHERE usuario=?", [usuario])
        if cursor.fetchone() is not None:
            messagebox.showerror("Erro", "Usuario ja cadastrado.")
        else:
            cursor.execute("INSERT INTO usuarios VALUES(?, ?)", [usuario, senha])
            conn.commit()
            messagebox.showinfo("Sucesso","Conta criada.")
    else:
        messagebox.showerror("Erro","Coloque todos os dados.")

def logar_conta():
    usuario = usuario_entry2.get()
    senha = senha_entry2.get()
    if usuario != "" and senha != "":
        cursor.execute("SELECT senha FROM usuarios WHERE usuario=?", [usuario])
        result = cursor.fetchone()
        if result:
            if senha == result[0]:
                messagebox.showinfo("Sucesso","Logado com sucesso.")
                if funcionario == "off":
                    new()
                elif funcionario == "on":
                    news()
            else:
                messagebox.showerror("Erro","Senha invalida.")
        else:
            messagebox.showerror("Erro","Usuario invalido.")
    else:
        messagebox.showerror("Erro","Entre todos os dados")

def new():
    guia1= customtkinter.CTkToplevel(app, fg_color="#56727b")
    guia1.title("Cadastro")
    guia1.geometry("500x300")
    guia1.resizable(False, False)
    guia1.grab_set()

    def clique():
        login_dig = login.get()
        senha_dig = senha.get()
        if login_dig in logins:
            print("Login ja cadastrado.")
        else:
            logins.append(login_dig)
            senhas.append(senha_dig)
        login.delete(0, 'end')  # Limpa o campo de email
        senha.delete(0, 'end')  # Limpa o campo de senha

    def click():
        print(logins)
        print(senhas)

    texto = customtkinter.CTkLabel(guia1, text="Cadastro")

    login = customtkinter.CTkEntry(guia1, placeholder_text="Login", fg_color="#56727b", border_color="#304146",
                                   border_width=2, font=("Arial", 15), text_color="#ffffff")

    senha = customtkinter.CTkEntry(guia1, placeholder_text="Senha", show="*", fg_color="#56727b",
                                   border_color="#304146",
                                   border_width=2, font=("Arial", 15), text_color="#ffffff")

    botao = customtkinter.CTkButton(guia1, text="Cadastrar", command=clique, corner_radius=32, fg_color="#56727b",
                                    hover_color="#2a3536", border_color="#304146", border_width=2, font=("Arial", 15))

    botao2 = customtkinter.CTkButton(guia1, text="Checar", command=click, corner_radius=32, fg_color="#56727b",
                                     hover_color="#2a3536", border_color="#304146", border_width=2, font=("Arial", 15))

    texto.pack(padx=10, pady=10)
    login.pack(padx=10, pady=10)
    senha.pack(padx=10, pady=10)
    botao.pack(padx=10, pady=10)
    botao2.pack(padx=10, pady=10)

def news():
    guia2= customtkinter.CTkToplevel(app, fg_color="#2a3536")
    guia2.title("Avaliação")
    guia2.geometry("500x300")
    guia2.resizable(False, False)
    guia2.grab_set()

    def home():
        guia2.destroy()
        guia2.update()

    def click():
        avaliação = slider.get()
        print(avaliação)

    texto = customtkinter.CTkLabel(guia2, text="Avaliação de Produto")
    texto.pack(padx=10, pady=10)

    slider = customtkinter.CTkSlider(master=guia2, from_=1, to=5, number_of_steps=4, button_color="#56727b",
                                     progress_color="#304146")
    slider.pack(padx=10, pady=10)

    botao2 = customtkinter.CTkButton(guia2, text="Checar", command=click, corner_radius=32, fg_color="#56727b",
                                     hover_color="#2a3536", border_color="#304146", border_width=2, font=("Arial", 15))
    botao2.pack(padx=10, pady=10)

def login():
    frame1.destroy()
    frame2 = customtkinter.CTkFrame(app, bg_color="#001220", fg_color="#001220",width=470,height=360)
    frame2.place(x=0,y=0)

    image1 = PhotoImage(file="projeto/message_icon.png", width=150, height=360)
    image1_label = Label(frame2, image=image1,bg="#001220")
    image1_label.place(x=0, y=0)
    frame2.image1 = image1

    login_label2 = customtkinter.CTkLabel(frame2, font=font1, text="Entrar",text_color="#fff", bg_color="#001220")
    login_label2.place(x=280,y=20)

    global usuario_entry2
    global senha_entry2

    usuario_entry2 = customtkinter.CTkEntry(frame2, font=font2, text_color="#fff", fg_color="#001a2e", bg_color="#121111", border_color="#004780", border_width=3,placeholder_text="Usuario",placeholder_text_color="#a3a3a3", width=200, height=50)
    usuario_entry2.place(x=230,y=80)

    senha_entry2 = customtkinter.CTkEntry(frame2, font=font2,show="*", text_color="#fff", fg_color="#001a2e", bg_color="#121111", border_color="#004780", border_width=3,placeholder_text="Usuario",placeholder_text_color="#a3a3a3", width=200, height=50)
    senha_entry2.place(x=230,y=150)

    login_botao2 = customtkinter.CTkButton(frame2,font=font2,command=logar_conta,text_color="#00bf77",text="Login",fg_color="#001220",hover_color="#006e44",bg_color="#121111",cursor="hand2",width=40)
    login_botao2.place(x=230, y=220)

frame1 = customtkinter.CTkFrame(app,bg_color="#001220",fg_color="#001220", width=470,height=360)
frame1.place(x=0, y=0)

image1 = PhotoImage(file="projeto/message_icon.png", width=150, height=360)
image1_label = Label(frame1, image=image1,bg="#001220")
image1_label.place(x=0, y=0)

cadastro_label = customtkinter.CTkLabel(frame1, font=font1, text="Cadastro",text_color="#fff", bg_color="#001220")
cadastro_label.place(x=280,y=20)

usuario_entry = customtkinter.CTkEntry(frame1, font=font2, text_color="#fff",fg_color="#001a2e",bg_color="#121111",border_color="#004780",border_width=3,placeholder_text="Username",placeholder_text_color="#a3a3a3",width=200,height=50)
usuario_entry.place(x=230,y=80)

senha_entry = customtkinter.CTkEntry(frame1, font=font2, text_color="#fff",show="*",fg_color="#001a2e",bg_color="#121111",border_color="#004780",border_width=3,placeholder_text="Password",placeholder_text_color="#a3a3a3",width=200,height=50)
senha_entry.place(x=230,y=150)

cadastro_botao = customtkinter.CTkButton(frame1,font=font2,command=cadastro ,text_color="#fff",text="Cadastro",fg_color="#00965d",hover_color="#006e44",bg_color="#121111",cursor="hand2",corner_radius=5,width=120)
cadastro_botao.place(x=230, y=260)

login_label = customtkinter.CTkLabel(frame1, font=font3, text="Ja tem uma conta?",text_color="#fff", bg_color="#001220")
login_label.place(x=230,y=290)

login_botao = customtkinter.CTkButton(frame1,command=login,font=font4,text_color="#00bf77",text="Login",fg_color="#001220",hover_color="#006e44",bg_color="#121111",cursor="hand2",width=40)
login_botao.place(x=355, y=290)

funcionario = customtkinter.StringVar(value="off")
checkbox = customtkinter.CTkCheckBox(app, text_color="#fff",text="É funcionario?",fg_color="#00965d",hover_color="#006e44",bg_color="#121111",cursor="hand2",corner_radius=5,width=120,font=font3, command=checkbox_event,
                                     variable=funcionario, onvalue="on", offvalue="off")
checkbox.place(x=230,y=220)

app.mainloop()
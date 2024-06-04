import customtkinter
import sqlite3
from tkinter import *
from tkinter import messagebox



customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")
janela.title("Cadastro de Clientes")

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS users(
               username TEXT NOT NULL,
               password TEXT NOT NULL)'''
               )

logins = []
senhas = []

texto = customtkinter.CTkLabel(janela, text="Bem vindo a ######")
texto.pack(padx=10, pady=10)

def new():
    guia1= customtkinter.CTkToplevel(janela, fg_color="#56727b")
    guia1.title("Cadastro")
    guia1.geometry("500x300")
    guia1.resizable(False, False)
    guia1.grab_set()

    def home():
        guia1.destroy()
        guia1.update()

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

    voltar = customtkinter.CTkButton(guia1, text="Voltar para home", command=home)
    voltar.pack(padx=10, pady=10)

def news():
    guia2= customtkinter.CTkToplevel(janela, fg_color="#2a3536")
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


    voltar = customtkinter.CTkButton(guia2, text="Voltar para home", command=home)
    voltar.pack(pady=30)

button = customtkinter.CTkButton(janela, text="Cadastro e login", command=new)
button.pack(pady=40)

button2 = customtkinter.CTkButton(janela, text="Avaliação", command=news)
button2.pack(pady=20)


janela.mainloop()

import os

db_path = os.path.abspath('data.db')
print("Caminho completo para o arquivo 'data.db':", db_path)

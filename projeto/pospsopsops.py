import customtkinter

customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")
janela.title("Cadastro de Clientes")

logins = []
senhas = []


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


texto = customtkinter.CTkLabel(janela, text="Cadastro")

login = customtkinter.CTkEntry(janela, placeholder_text="Login", fg_color="#56727b", border_color="#304146",
                               border_width=2, font=("Arial", 15), text_color="#ffffff")

senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*", fg_color="#56727b", border_color="#304146",
                               border_width=2, font=("Arial", 15), text_color="#ffffff")

botao = customtkinter.CTkButton(janela, text="Cadastrar", command=clique, corner_radius=32, fg_color="#56727b",
                                hover_color="#2a3536", border_color="#304146", border_width=2, font=("Arial", 15))

botao2 = customtkinter.CTkButton(janela, text="Checar", command=click, corner_radius=32, fg_color="#56727b",
                                 hover_color="#2a3536", border_color="#304146", border_width=2, font=("Arial", 15))

texto.pack(padx=10, pady=10)
login.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)
botao2.pack(padx=10, pady=10)

janela.mainloop()
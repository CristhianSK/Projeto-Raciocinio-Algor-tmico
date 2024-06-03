import customtkinter
from PIL import Image
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")

emails = []
senhas = []

def clique():
    email_dig = email.get()
    senha_dig = senha.get()
    emails.append(email_dig)
    senhas.append(senha_dig)
    email.delete(0, 'end')  # Limpa o campo de email
    senha.delete(0, 'end')  # Limpa o campo de senha
    


def click():
    print(emails)
    print(senhas)
texto = customtkinter.CTkLabel(janela, text="Fazer Login")

email = customtkinter.CTkEntry(janela, placeholder_text="Email",)

senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")

botao = customtkinter.CTkButton(janela, text="Login", command=clique, corner_radius=32, fg_color="#4c5966", font=("Arial", 15))

botao2 = customtkinter.CTkButton(janela, text="Checar", command=click, corner_radius=32, fg_color="#4c5966")

texto.pack(padx=10, pady=10)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)
botao2.pack(padx=10, pady=10)

janela.mainloop()
import customtkinter

customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")
janela.title("Cadastro de Clientes")

def new():
    guia1= customtkinter.CTkToplevel(janela, fg_color="#56727b")
    guia1.title("Nova Guia!")
    guia1.geometry("500x300")
    guia1.resizable(False, False)

    def home():
        guia1.destroy()
        guia1.update()

    voltar = customtkinter.CTkButton(guia1, text="Voltar para home", command=home)
    voltar.pack(pady=30)

def news():
    guia2= customtkinter.CTkToplevel(janela, fg_color="#2a3536")
    guia2.title("Guia 223223!")
    guia2.geometry("500x300")
    guia2.resizable(False, False)

    def home():
        guia2.destroy()
        guia2.update()

    voltar = customtkinter.CTkButton(guia2, text="Voltar para home", command=home)
    voltar.pack(pady=30)

button = customtkinter.CTkButton(janela, text="Abrir nova guia", command=new)
button.pack(pady=40)

button2 = customtkinter.CTkButton(janela, text="Abrir guia 2", command=news)
button2.pack(pady=20)


janela.mainloop()
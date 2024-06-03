import customtkinter 


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")
janela.title("Avaliação de Produto")

def click():
    avaliação = slider.get()
    print(avaliação)

texto = customtkinter.CTkLabel(janela, text="Avaliação de Produto")
texto.pack(padx=10, pady=10)        

slider = customtkinter.CTkSlider(master=janela, from_=1, to=5, number_of_steps=4, button_color="#56727b", progress_color="#304146")
slider.pack(padx=10, pady=10)

botao2 = customtkinter.CTkButton(janela, text="Checar", command=click, corner_radius=32, fg_color="#56727b",hover_color="#2a3536",border_color="#304146",border_width=2, font=("Arial", 15))
botao2.pack(padx=10, pady=10)

janela.mainloop()
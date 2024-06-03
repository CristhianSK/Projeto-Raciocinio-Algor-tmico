import customtkinter
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark")
janela = customtkinter.CTk()
janela.geometry("500x300")

janela.mainloop()


estoque = {}
avaliação = {}
usuarios = {}
projeto = [usuarios, estoque, avaliação]
print("Bem Vindo a Tupac Store!\nO que deseja fazer?")
esc = input("=-=-=-=-=-=-=-\n1 - Checar ou cadastrar usuarios\n2 - Conferir estoque\n3 - Avaliar produto\n=-=-=-=-=-=-=-\n")
if esc == "1":
    print("-=" * 12)
    print("  Cadastro de Clientes")
    print("=-" * 12)
    while True:
        cliente = input("Digite o nome do cliente a ser cadastrado (0 para sair): ")
        if cliente in usuarios:
            if input("Cliente ja cadastrado, deseja alterar os dados?") == "nao":
                continue
        if cliente == "0": break
        numero = input("Digite o numero do contato: ")
        if numero in usuarios.values():
            print("Telefone ja cadastrado em outro contato.")
            continue
        usuarios[cliente] = numero
    print(usuarios)
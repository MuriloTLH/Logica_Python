def menu():
    print("\nMenu:")
    print("0 - Adicionar filme (opcional)")
    print("1 - Quantidade total de filmes")
    print("2 - Informações de um filme pelo título")
    print("3 - Filmess de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - Média de duração dos filmes")
    print("6 - Sair")

while True:
    menu()
    opc = input("Escolha uma opção: ").strip

    if opc == "0":
        print("adicionar filme()")
    elif opc == "1":
        print("contar_filmes()")
    elif opc == "2":
        print("info_por_titulo()")
    elif opc == "3":
        print("filmes_por_diretor()")
    elif opc == "4":
        print("filmes_por_genero()")
    elif opc == "5":
        print("media_duracao()")
    elif opc == "6":
        print("Saindo . . .")
        break
    else:
        print("Opção invalida. Tente novamente.")
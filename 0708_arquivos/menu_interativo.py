def menu():
    print("\nMenu:")
    print("0 - Adicionar filme (opcional)")
    print("1 - Quantidade total de filmes")
    print("2 - Informações de um filme pelo título")
    print("3 - Filmess de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - Média de duração dos filmes")
    print("6 - Sair")

def adicionar_filme():
    print("Adicionar filme")

def contar_filmes():

    print("Contar filmes\n")

    total_filmes = 0 
    
    with open('arq_filme.txt', 'r', encoding='utf-8') as f:
        for linha in f:
            linha_limpa = linha.strip()
            
            print(linha_limpa)
            
            if "Título" in linha_limpa:
                total_filmes += 1 
                
    print(f"\nTotal de filmes encontrados: {total_filmes}")


def info_por_titulo():
    titulo_busca = input("Digite o título do filme: ").strip().lower()
    encontrado = False
    try:
        with open('arq_filme.txt', 'r', encoding='utf-8') as f:
            for linha in f:
                if linha.strip().startswith("Título:"):
                    titulo = linha.split(":", 1)[1].strip()
                    if titulo.lower() == titulo_busca:
                        print(f"Título: {titulo}")
                        try:
                            ano = next(f).strip()
                            diretor = next(f).strip()
                            genero =  next(f).strip()
                            duracao =  next(f).strip()
                        except StopIteration:
                            print("Registro incompleto para esse título.")
                            return
    
                        print(ano)
                        print(diretor)
                        print(genero)
                        print(duracao)
                        encontrado = True
                        break

    except FileNotFoundError:
        print("Arquivo 'arq_filme.txt' não encontrado")
        return




    # print("Info por título")
    # nome = input("Digite o título do filme: ")

    # encontrado = False 

    # with open('arq_filme.txt', 'r', encoding='utf-8') as f:

    #     for linha in f:
    #         linha_limpa = linha.strip()
    #         if nome in linha_limpa:

    #             encontrado = True

    #             print(linha_limpa)
                
    #             next(f)
    #         else:
    #             print("Título não encontrado...")
    #             break
    #         menu()


def filmes_por_diretor():
    print("Filmes por diretor")

def filmes_por_genero():
    print("Filmes por genero")

def media_duracao():
    print("Média da duração")

while True:
    menu()
    opc = input("Escolha uma opção: ").strip()
    if opc == "0":
        adicionar_filme()         
    elif opc == "1":
        contar_filmes()
    elif opc == "2":
        info_por_titulo()
    elif opc == "3":
        filmes_por_diretor()
    elif opc == "4":
        filmes_por_genero()
    elif opc == "5":
        media_duracao()
    elif opc == "6":
        print("Saindo . . .")
        break
    else:
        print("Opção invalida. Tente novamente.")
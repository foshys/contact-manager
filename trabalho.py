#João Victor Fernandes Martins
#Alef Emanuel Marques Verissimo

import re

dicionario_contato = {
    "Nome do Contato": [],
    "Telefone do contato": []
}

def validar_str(valor):
    return valor.isalpha()

def validar_telefone(telefone):
    return re.match(r"^\+\d{2} \d{10}$", telefone)


def add_contato(nome, telefone):
    if not validar_str(nome.replace(" ", "")):
        print("Nome inválido, deve ser uma série de letras.")
        return


    if not validar_telefone(telefone):
        print("Contato inválido, deve conter o prefixo do país e DDD.")
        return

 
    dicionario_contato["Nome do Contato"].append(nome)
    dicionario_contato["Telefone do contato"].append(telefone)
    print("Contato adicionado com sucesso!")

def pesquisar_contato(contato):
    contatos_encontrados = []

    print("LISTA DE CONTATOS:")

    for i, Searchednumber in enumerate(dicionario_contato["Nome do Contato"]):

        if contato in Searchednumber:
            contatos_encontrados.append({
                "Nome": dicionario_contato["Nome do Contato"][i],
                "Telefone": dicionario_contato["Telefone"][i]
            })

    return contatos_encontrados

def remover_contato(contato):
    if contato in dicionario_contato["Telefone do contato"]:
        index = dicionario_contato["Telefone do contato"].index(contato)

        for key in dicionario_contato.keys():
            dicionario_contato[key].pop(index)

        print("Contato removido com sucesso!")

    else:
        print("Contato não encontrado, digite um contato válido!")

def menu_sistema():
    while True:
        escolha = input("SEJA BEM VINDO AO SISTEMA DE GERENCIAMENTO DE CONTATOS!\n"
                        "\n 1) Adicionar novo contato "
                        "\n 2) Pesquisar por contato "
                        "\n 3) Excluir por contato "
                        "\n 4) Sair do Sistema\n"
                        "\n Escolha uma das opções acima: ")

        if escolha.isdigit():
            menu = int(escolha)

            if menu == 1:
                nome = input("Digite o nome do contato: ")
                telefone = input("Digite o telefone para o contato (+XX XXXXXXXXXX): ")
                add_contato(nome, telefone)

            elif menu == 2:
                contato = input("Digite o contato que deseja pesquisar: ")
                contatos = pesquisar_contato(contato)

                for contato in contatos:
                    print(contato)

            elif menu == 3:
                contato = input("Digite o contato que deseja remover: ")
                remover_contato(contato)

            elif menu == 4:
                print("Obrigado por usar o nosso sistema")
                break

            else:
                print("Opção inválida. Tente novamente.")
        else:
            print("Opção Invalida. Por favor, digite um número de 1 a 4.")


menu_sistema()
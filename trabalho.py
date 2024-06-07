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

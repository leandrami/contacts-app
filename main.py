#  -- FUNÇÕES --
def adicionar_contato (lista_contatos , nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False} #dicionario q fará parte da lista
    lista_contatos.append (contato)   #lista de contatos
    
    print (f"O contato {nome} foi adicionado com sucesso!")
    return

def listar_contatos (lista_contatos):
    lista_contatos.sort(key=lambda contato: contato['nome'].lower()) # ordena a lista em ordem alfábética
    print (f"\n Lista de Contatos: ")
    for indice, contato in enumerate (lista_contatos, start=1):    # cada item recebe um indice relacionado
        status = "★" if contato["favorito"] else " "
        print(f"{indice}. - [{status}] {contato['nome']} - {contato['telefone']}")
    
    return




def renomear_contato (lista_contatos, indice_contato, novo_nome_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(lista_contatos): 
        lista_contatos[indice_contato_ajustado]['nome'] = novo_nome_contato
        print (f"O Contato {indice_contato} foi renomeado para o {novo_nome_contato} ")
        
    else :
        print ("Número do contato inválido.")
    return








#  -- MENU --
lista_contatos = []
while True:
    print ("\nMenu do App Contatos:")
    print ("1 - Adicionar contato")
    print ("2 - Ver contato")
    print ("3 - Renomear contato")
    print ("4 - Favoritar contato")
    print ("5 - Ver contatos favoritos")
    print ("6 - Apagar um contato")
    print ("7 - Sair")
    
    escolha = input("Digite a opção desejada: ")

    if (escolha == "1") :
        nome = input ("Digite o nome do contato: ")
        telefone = input ("Digite o telefone: ")
        email = input ("Digite o e-mail: ")
        adicionar_contato (lista_contatos , nome, telefone, email)    
        
    elif (escolha == "2") :
        listar_contatos(lista_contatos)
        
    elif (escolha == "3") :
        listar_contatos(lista_contatos)
        indice_contato = input ("Digite o número do contato que deseja renomear:")
    
        novo_nome_contato = input("Digite o novo nome do contato: ")
        renomear_contato (lista_contatos, indice_contato, novo_nome_contato)
        
        
        
        
        
        
        
        
        
    elif (escolha == "7"):
        break

print (f"Agenda de contatos finalizada.\nLista de contatos: ", lista_contatos)
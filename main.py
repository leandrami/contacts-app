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
        lista_contatos[indice_contato_ajustado]['nome'] = novo_nome_contato   #lista[indice][chave] -> acessa elemento específico dentro do dicionário e atualiza o nome
        print (f"O Contato {indice_contato} foi renomeado para o {novo_nome_contato} ")
        
    else :
        print ("Número do contato inválido.")
    return



def favoritar_contato (lista_contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >=0 and indice_contato_ajustado < len(lista_contatos):
        lista_contatos [indice_contato_ajustado] ["favorito"] = True  #lista[indice][chave] -> acessa elemento específico dentro do dicionário e atualiza a chave 'favorito'
        print (f"Contato {indice_contato} marcado com favorito!")
    else :
        print ("Indice do contato inválido.")
    return

def listar_favoritos(lista_contatos): 
    print("\nContatos favoritos:")
    for indice, contato in enumerate(lista_contatos, start=1):
        if contato["favorito"]:
            status = "★"
            print(f"{indice}. - [{status}] {contato['nome']} - {contato['telefone']}")
    return

def deletar_contato(lista_contatos,indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(lista_contatos):
    lista_contatos.pop(indice_contato_ajustado)
    print (f"Contato N° {indice_contato} deletado com sucesso!")
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
    if escolha not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Opção inválida.")
        continue

    if (escolha == "1") :
        nome = input ("Digite o nome do contato: ")
        if not nome.strip():
            print("O nome não pode ficar vazio.")
            continue
        
        telefone = input ("Digite o telefone: ")
        if not telefone.strip():
            print("O telefone não pode ficar vazio.")
            continue
        
        email = input ("Digite o e-mail: ")
        if not email.strip():
            print("O email não pode ficar vazio.")
            continue
        
        adicionar_contato (lista_contatos , nome, telefone, email) 
        
        
        
    elif (escolha == "2") :
        listar_contatos(lista_contatos)
        
    elif (escolha == "3") :
        listar_contatos(lista_contatos)
        indice_contato = input ("Digite o número do contato que deseja renomear:")
    
        novo_nome_contato = input("Digite o novo nome do contato: ")
        renomear_contato (lista_contatos, indice_contato, novo_nome_contato)
        
        
    elif (escolha == "4") :
        listar_contatos (lista_contatos)
        indice_contato = input ("Digite o número do contato que deseja favoritar: ")
        favoritar_contato (lista_contatos, indice_contato)
        
    elif (escolha == "5"):
        listar_favoritos(lista_contatos)    
        
    elif (escolha == "6"):
        listar_contatos (lista_contatos)
        indice_contato = input ("Digite o número do contato que deseja excluir: ")
        deletar_contato(lista_contatos, indice_contato)
        
        
    elif (escolha == "7"):
        break

print (f"Agenda de contatos finalizada.\nLista de contatos: ", lista_contatos)
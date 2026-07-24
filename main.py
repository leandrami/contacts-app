#  -- FUNÇÕES --
def adicionar_contato (lista_contatos , nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    lista_contatos.append (contato)
    
    print (f"O contato {nome} foi adicionado com sucesso!")
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
        print (f"O contato {nome} foi adicionado com sucesso!")
        
        
        
        
    elif (escolha == "7"):
        break

print (f"Agenda de contatos finalizada.\nLista de contatos: ", lista_contatos)
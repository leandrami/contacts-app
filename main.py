#  -- FUNÇÕES --
def adicionar_contato (lista_contatos , nome_contato):
    contato {"nome": nome_contato, "telefone": telefone, "email": email, "favorito": False}
    lista_contatos.append (contato)
    
    print (f"O contato {nome_contato} foi adicionado com sucesso!")
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
    
    
escolha = input(" Digite a opção desejada: ")

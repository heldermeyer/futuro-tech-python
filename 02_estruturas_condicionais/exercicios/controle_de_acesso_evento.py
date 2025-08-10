# Controle de Acesso a um Evento

idade = True if int(input("Informe a sua idade: ")) >= 18 else False
traje_social = True if input("Informe se você está usando traje social (S/N): ").lower() == "s" else False
lista_vip = True if input("Informe o seu nome: ").lower() in ["helder"] else False

if (idade) and (traje_social or lista_vip): print("Acesso permitido!")
else:
    if idade == False: print("Acesso negado! Usuário é menor de idade!")
    else: print("Acesso negado! Usuário não está na lista ou não está usando traje social!")
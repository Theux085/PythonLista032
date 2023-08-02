nome = input("Digite o seu primeiro nome: ")
idade = int ( input("Digite sua idade: "))

#print("Ola ", nome, "!")
#print("Tudo bem com voce?")
#print("Caramba", nome, "! Voce tem", idade, "anos? Nem parece.")

print("Ola , {}!".format(nome))
print("Tudo bem com voce?")
print("Caramba {}! Voce tem {} anos? Nem parece.".format(nome, idade))

valor = float(input("Qual é o valor normal da prestaçao?"))
taxa = float(input("Qual é a taxa de juros?"))
tempo = float(input("Quantos dias de atraso?"))
prestacao = valor + (valor * (taxa/100) * tempo)
print("O valor da prestaçao em atraso é R$", prestacao)


valor1 = 8.75217
valor2 = 73932.6
valor3 = 11.349
#formatação apenas como valor float
print("Valor 1: (:f)".format(valor1))
#formatação float com decinal es 2 dígitos
print("Valor 1: (:.2f) ".format (valor1))
print("Valor 2: (:.2f)-".format (valor2))
print("Valor 3: (:.2f).".format (valor3))

#formatação float com separador de milhares
# e decinal en 2 dígitos
print("Valor 2: (: ,.2f) " .format (valor2))

# __________________________________
# formatação float, com total de 10 digitos (numeros e pontos), sendo 2 decimais
print("Valor 1: {:010.2f}".format(valor1))
print("Valor 2: {:010.2f}".format(valor2))
print("Valor 3: {:010.2f}".format(valor3))

#senelhante ao anterior, mas preencha casas antes do ponto com zero
print("Valor 1: {:010.2f}".format(valor1))
print("Valor 2: {:010.2f}".format(valor2))
print("Valor 3: {:010.2f}".format(valor3))

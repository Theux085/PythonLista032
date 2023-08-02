valor1 = 8.75217
valor2 = 73932.6
valor3 = 11.349
# formatação apenas como valor float
print(f"Valor 1: {valor1:f}")
# formatação float com decinal es 2 dígitos
print(f"Valor 1: {valor1:.2f} ")
print(f"Valor 2: {valor2:.2f}")
print(f"Valor 3: {valor3:.2f}.")

# formatação float com separador de milhares e decinal en 2 dígitos
print(f"Valor 2: {valor2:,.2f} ")

# __________________________________
# formatação float, com total de 10 digitos (numeros e pontos), sendo 2 decimais
print(f"Valor 1: {valor1:010.2f}")
print(f"Valor 2: {valor2:010.2f}")
print(f"Valor 3: {valor3:010.2f}")

# senelhante ao anterior, mas preencha casas antes do ponto com zero
print(f"Valor 1: {valor1:010.2f}")
print(f"Valor 2: {valor2:010.2f}")
print(f"Valor 3: {valor3:010.2f}")

valor4 = 0.7536

# Formataçao float exibindo em percentual com decimal em 1 digito
print(f"Valor 4: {valor4:.1%}")

# Incluindo R$ antes do valor e substituindo a virgula do milhar por underline
texto_valor2 = f"R$ {valor2:_.2f}"
print(f"Texto Valor 2: {texto_valor2}")

# Substituindo o que é ponto por vírgula e o que é underline por ponto
texto_valor_br = texto_valor2.replace(".",",").replace("_",".")
print(f"Texto valor Br: {texto_valor_br}")



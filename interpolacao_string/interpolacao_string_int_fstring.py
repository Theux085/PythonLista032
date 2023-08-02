num1 = 6
num2 = 382

# Simboliza-se a formataçao int com:d (de digito)
print(f"num1: {num1:d}".format(num1)) # apenas int.

print(f"num1: {num1:7d}") # int com 7 digitos
print(f"num2: {num2:7d}")

print(f"num1: {num1:07d}") # int 7 digitos, preenchendo com zeros.
print(f"num2: {num2:07d}")
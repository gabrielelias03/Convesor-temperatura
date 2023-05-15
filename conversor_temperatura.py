# Pedir a temperatura e a escala de temperatura atual
temperatura = float(input("Insira a temperatura: "))
escala = input("Insira a escala de temperatura (Celsius ou Fahrenheit): ")

# Converter Celsius para Fahrenheit
if escala == "Celsius":
    resultado = (temperatura * 9/5) + 32
    nova_escala = "Fahrenheit"
    print(f"{temperatura} graus Celsius equivale a {resultado} graus Fahrenheit.")
# Converter Fahrenheit para Celsius
elif escala == "Fahrenheit":
    resultado = (temperatura - 32) * 5/9
    nova_escala = "Celsius"
    print(f"{temperatura} graus Fahrenheit equivale a {resultado} graus Celsius.")
# Caso a escala inserida seja inválida
else:
    print("A escala de temperatura inserida é inválida. Tente novamente.")

personas_autorizadas = ["Alberto", "Carmen"]
nombre = input("Dígame su nombre: ")
if nombre in personas_autorizadas:
    print("Está autorizado")
else:
    print("No está autorizado")
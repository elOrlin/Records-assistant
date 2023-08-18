from Usuarios import acciones

print("""
Acciones disponibles:
    -Registro
    -Login
""")

verificado = acciones.Acciones()

accion = input("Que quieres hacer?")

if accion == 'Registro':
    verificado.registro()

elif accion == 'Login':
    verificado.login()
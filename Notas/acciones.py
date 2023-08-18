import Notas.notas as modelo

class Acciones:

    def crear(self, usuario):
        print(f'Ok {usuario[1]} Vamos a crear una nueva nota...')
        titulo = input('Introduce el titulo de tu nota:')
        description = input('Agrega el contenido de tu nota:')

        nota = modelo.Nota(usuario[0], titulo, description)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f'Perfecto has guardado la nota: {nota.titulo}')
        else:
            print(f'No se ha guardado la nota, lo siento {usuario[1]}')

    def mostrar(self, usuario):
        print(f"Vale {usuario[1]}!! Aqui tienes tus notas:")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n*******************************")
            print(nota[2])
            print(nota[3])
            print("*******************************")

    def eliminar(self, usuario):
        print(f"\n Okay {usuario[1]}!! vamos a borrar notas")

        titulo = input("Introduce el titulo de la nota a borrar")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos  borrado la nota: {nota.titulo}")

        else:
            print("No se ha borrado la nota, prueba luego...")

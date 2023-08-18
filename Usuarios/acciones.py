import Usuarios.usuarios as modelo
import Notas.acciones

class Acciones:

    def registro(self):
        print('OK Vamos a registrarse en el sistema')
        nombre = input('Cual es tu nombre?')
        apellidos = input('Cuales son tus apellidos?')
        email = input('Introduce tu email')
        password = input('Introduce tu password')

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f'Perfecto, {registro[1]} te has registrado con el email {usuario[1].email}')

        else:
            print('No te has registrado correctamente')

    def login(self):
        print('Vale Identificate en el sistema')

        try:
            email = input('Introduce tu email')
            password = input('Introduce tu password')

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f'Bienvenido {login[1]} te has registrado en el sistema el {login[5]}')
                self.proximasAcciones(login)

        except Exception as e:
            print(e)
            print(type(e).__name__)
            print(f'Login incorrecto! Intentalo mas tarde')

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)

        accion = input('Que quieres hacer?')

        verificado = Notas.acciones.Acciones()

        if accion == 'crear':
            verificado.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'mostrar':
            verificado.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'eliminar':
            verificado.eliminar(usuario)
            self.proximasAcciones(usuario)

        elif accion == 'salir':
            print(f'{usuario[1]}, hasta pronto')
            exit()
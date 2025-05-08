import sqlite3
import hashlib

# -------- ENCRIPTAR CONTRASEÑA --------
def obtener_hash_contrasena(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# -------- CREAR BASE DE DATOS Y TABLA --------
def crear_base_y_tabla():
    conexion = sqlite3.connect('Usuarios_Xbox.db')  # Nuevo nombre de la base de datos
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tabla_usuarios (
            identificador INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_usuario TEXT NOT NULL UNIQUE,
            nombre_completo TEXT,
            correo_electronico TEXT,
            numero_contacto TEXT,
            direccion_residencial TEXT,
            clave_cifrada TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()
    print("✅ Base de datos y tabla listas.")

# -------- INSERTAR USUARIO --------
def insertar_usuario_interactivo():
    print("\n📝 Agregar nuevo usuario")
    usuario = input("Nombre de usuario: ")
    contrasena = input("Contraseña: ")
    nombre = input("Nombre completo: ")
    correo = input("Correo electrónico: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    
    hash_clave = obtener_hash_contrasena(contrasena)
    datos_usuario = (usuario, nombre, correo, telefono, direccion, hash_clave)

    try:
        conexion = sqlite3.connect('Usuarios_Xbox.db')  # Nuevo nombre de la base de datos
        cursor = conexion.cursor()
        consulta = '''
            INSERT INTO tabla_usuarios (
                nombre_usuario, nombre_completo, correo_electronico,
                numero_contacto, direccion_residencial, clave_cifrada
            ) VALUES (?, ?, ?, ?, ?, ?)
        '''
        cursor.execute(consulta, datos_usuario)
        conexion.commit()
        print(f"✅ Usuario '{usuario}' insertado correctamente.")
    except sqlite3.IntegrityError:
        print(f"⚠️  El nombre de usuario '{usuario}' ya existe.")
    finally:
        conexion.close()

# -------- CONSULTAR USUARIO --------
def buscar_usuario(nombre_usuario):
    conexion = sqlite3.connect('Usuarios_Xbox.db')  # Nuevo nombre de la base de datos
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tabla_usuarios WHERE nombre_usuario = ?", (nombre_usuario,))
    resultado = cursor.fetchone()
    conexion.close()
    return resultado

# -------- MOSTRAR DATOS DEL USUARIO --------
def mostrar_datos_usuario(datos):
    campos = [
        "ID", "Usuario", "Nombre completo", "Correo electrónico",
        "Teléfono", "Dirección", "Hash de contraseña"
    ]
    print("\n📋 Información del usuario:")
    for campo, valor in zip(campos, datos):
        print(f"{campo}: {valor}")

# -------- MENÚ PRINCIPAL --------
def main():
    crear_base_y_tabla()

    while True:
        print("\n📘 Menú de opciones")
        print("1. Consultar usuario")
        print("2. Agregar nuevo usuario")
        print("3. Salir")

        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == "1":
            nombre_usuario = input("🔍 Introduce el nombre de usuario a consultar: ")
            resultado = buscar_usuario(nombre_usuario)
            if resultado:
                mostrar_datos_usuario(resultado)
            else:
                print("❌ Usuario no encontrado.")
        elif opcion == "2":
            insertar_usuario_interactivo()
        elif opcion == "3":
            print("👋 Saliendo del programa.")
            break
        else:
            print("⚠️  Opción no válida. Intenta de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()

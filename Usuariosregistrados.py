import sqlite3

def mostrar_usuarios_registrados():
    conexion = sqlite3.connect('Usuarios_Xbox.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tabla_usuarios")
    filas = cursor.fetchall()
    conexion.close()

    print("\n📋 Usuarios registrados:")
    for fila in filas:
        print(fila)

mostrar_usuarios_registrados()


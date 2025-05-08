Usuarios Xbox – Gestión de Usuarios con Python y SQLite
Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar usuarios para un sistema ficticio llamado "Usuarios Xbox". Utiliza SQLite para almacenamiento local y ejecuta todo en un contenedor Docker.

¿Qué hace?
-Crea una base de datos Usuarios_Xbox.db con una tabla de usuarios.
-Permite insertar nuevos usuarios (con contraseña cifrada SHA-256).
-Permite consultar usuarios existentes por su nombre de usuario.

Estructura del proyecto
.
├── Dockerfile
├── FinalDEVOPS.py
├── Usuarios_Xbox.db
└── README.md

🐳 Cómo ejecutar con Docker
1-Construir la imagen
docker build -t usuarios-app .
2-Ejecutar el contenedor
 docker run -it usuarios-app
 La opción -it permite usar el programa de forma interactiva desde la terminal.

Requisitos (si no usas Docker)
-Python 3.10+
-SQLite3 (incluido en Python estándar)
Ejecuta el archivo directamente:
python FinalDEVOPS.py

Seguridad
Las contraseñas se almacenan cifradas usando el algoritmo SHA-256 mediante el módulo hashlib.

Licencia
Este proyecto es de uso educativo y puede modificarse libremente.






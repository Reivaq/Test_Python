# Test TCP: Servidor y Cliente en Python

Este repositorio contiene la implementación de un servidor y un cliente TCP en Python, diseñado como parte de un ejercicio técnico. Ambos, servidor y cliente, se comunican en localhost mediante el puerto 5000.

## Requisitos

- Python 3.x

### Crear un entorno virtual:

1. Abre la terminal y navega hasta el directorio del proyecto.
2. Ejecuta el siguiente comando para crear el entorno virtual:  
   `python -m venv ecoenv`

### Activar el entorno virtual:

- En **Windows**: `ecoenv\Scripts\activate`
- En **macOS/Linux**: `source ecoenv/bin/activate`

### Instalar dependencias con el archivo `requirements.txt`:

Ejecuta el comando:  
`pip install -r requirements.txt`

**Nota**: El archivo `requirements.txt` está vacío en este caso, ya que no se han instalado dependencias adicionales, pero este comando será útil si en el futuro se agregan librerías externas.

## Ejecución

1. Para iniciar el servidor, ejecuta el archivo `servicioTCP.py`.
2. Para iniciar el cliente, ejecuta el archivo `clienteTCP.py` en otra terminal.

## Pruebas Manuales

### Prueba de mayúsculas:

1. Ingresa un mensaje cualquiera desde el cliente.
2. Verifica que el servidor responda con el mensaje en **mayúsculas**.

### Prueba de desconexión:

1. Ingresa el comando `DESCONEXION` desde el cliente.
2. Verifica que tanto el cliente como el servidor cierren la conexión de manera correcta.

# Ejercicio TCP: Servidor y Cliente en Python

Este repositorio contiene una implementación de un servidor y cliente TCP en Python para un ejercicio técnico. El servidor y el cliente se comunican en `localhost` a través del puerto `5000`.

## Requisitos
- Python 3.x

1. **Crear un entorno virtual:**
   - Abre la terminal y en el directorio del proyecto.
   - Ejecutar: python -m venv ecoenv
2. **Activar el entorno virtual:**
   - En Windows:
     .ecoenv\Scripts\activate
   - En macOS/Linux:
     source ecoenv/bin/activate

3. **Instalar dependencias con el archivo `requirements.txt`:**
   - pip install -r requirements.txt
   - **Nota:** En este caso, el archivo `requirements.txt` está vacío porque no se instalaron dependencias adicionales, pero el comando sigue siendo útil si se agregan librerías externas en el futuro.

## Ejecución
1. Inicia el servidor ejecutando `servicioTCP.py`.
2. Inicia el cliente ejecutando `clienteTCP.py` en otra terminal.

## Pruebas Manuales
1. **Prueba de mayúsculas**:
   - Ingresar un mensaje cualquiera desde el cliente.
   - Verificar que el servidor responda con el mensaje en mayúsculas.

2. **Prueba de desconexión**:
   - Ingresar "DESCONEXION" en el cliente.
   - Verificar que el cliente y el servidor cierren la conexión correctamente.
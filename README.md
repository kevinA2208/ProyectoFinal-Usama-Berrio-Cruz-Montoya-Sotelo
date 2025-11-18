# ProyectoFinal-Usama-Berrio-Cruz-Montoya-Sotelo

## Guía de Instalación y Ejecución del Simulador de Ventas BigMart

Esta guía detalla el proceso para crear un entorno virtual de Python (venv), instalar las dependencias necesarias y ejecutar la aplicación web (API) de simulación de ventas basada en Flask.

### 1. Configuración del Entorno Virtual (VENV)


Un entorno virtual aísla las librerías de tu proyecto para evitar conflictos con otras instalaciones de Python en tu sistema.


Comando para Crear VENV en Windows

**python -m venv venv**

Comando para Crear VENV en macOS / Linux (Ubuntu)

**python3 -m venv venv**


### 2. Activación del Entorno

Una vez creado, debes "entrar" al entorno para que las librerías se instalen dentro de él.


Comando para Activar VENV en Windows (CMD o PowerShell)

**.\venv\Scripts\activate**

Comando para activar VENV en macOS / Linux (Ubuntu)

**source venv/bin/activate**


### 3. Instalación de Dependencias

Para que la aplicación funcione, necesita las librerías de ciencia de datos que utilizaste (Pandas, Scikit-Learn, Joblib) y el framework Flask.

Instalar las librerías usando el archivo requirements.txt

Con el entorno (venv) activo, ejecuta el siguiente comando:

pip install -r requirements.txt


### 4. Ejecución de la Aplicación Flask

Una vez que todas las librerías están instaladas y el entorno está activo, puedes iniciar el simulador.

Comando para Ejecutar: **python simulador_ventas/app.py** Se debe ejecutar desde la carpeta raiz

Acceso en el Navegador

Abre http://127.0.0.1:5000

Para Detener

Presiona Ctrl + C en la terminal.

### 5. Prueba del Simulador

Abre el navegador en la dirección indicada.

Ingresa datos de prueba (ej. Item_Type = Supermarket Type3, Item_MRP alto).

El sistema devolverá las Ventas Estimadas (el resultado de la transformación exponencial).

La predicción se hace principalmente en base a los datos del local, como el Tipo de tienda, La ubicación, el tamaño,
por lo que de esta forma, se podrían poner los datos de tiendas ya existentes, o de futuras tiendas creadas.

Importante: Si ves un error de "Error en el cálculo", asegúrate de que el prefijo del ID Producto sea obligatoriamente FD, DR o NC.
# Instrucciones para Usar el Código para Generar Etiquetas en PDF

Este código genera un archivo PDF con etiquetas que contienen información de modelos de zapatos, incluyendo el código de barras. A continuación, se explican los pasos a seguir para ejecutarlo correctamente:

## Requisitos Previos

1. **Python Instalado**: Se recomienda tener Python 3.9.7 o versiones superiores instaladas, aunque Python 3.9.7 ya está disponible en el entorno virtual, por lo que no es necesario instalarlo manualmente.

2. **Instalar pip**: Si aún no tienes `pip` instalado, puedes instalarlo con el siguiente comando:

   ```sh
   python -m ensurepip --default-pip
   ```

3. **Entorno Virtual**: La carpeta ya contiene un entorno virtual configurado. Para activarlo, usa el siguiente comando:

   - En Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   - En Linux/macOS:
     ```sh
     source venv/bin/activate
     ```

4. **Bibliotecas Necesarias**: Las bibliotecas necesarias ya están instaladas en el entorno virtual, por lo que no es necesario instalarlas manualmente.

5. **Archivo de Datos**: Debes tener un archivo Excel llamado `codigos_de_barras_pedidos.xlsx` que contenga dos columnas relevantes:
   - `identificador_del_producto`: Identificador del producto en un formato específico (por ejemplo, `FBAJV1003-NEGRO42`).
   - `CODIGO DE BARRAS`: Código de barras de 13 dígitos para cada producto.

## Estructura del Archivo Excel

El archivo Excel debe tener al menos dos columnas con estos nombres exactos:

- **identificador_del_producto**: El identificador tiene que seguir el formato `FBAJV1003-NEGRO42` para que el código pueda extraer el modelo, el color y la talla correctamente.
- **CODIGO DE BARRAS**: Debe contener códigos de barras de exactamente 13 dígitos.

## Ejecución del Código

1. Guarda el archivo Python y asegúrate de que el archivo Excel esté en el mismo directorio.
2. Activa el entorno virtual como se indicó anteriormente.
3. Ejecuta el script con el siguiente comando:

   ```sh
   python main.py
   ```

4. El código leerá los datos del archivo Excel, generará los códigos de barras y creará un archivo PDF con las etiquetas.

## Salida

- El archivo PDF con las etiquetas se generará en una carpeta llamada `etiquetas` y se llamará `etiquetas_zapatos_YYYYMMDD.pdf`, donde `YYYYMMDD` es la fecha actual.
- El PDF contendrá las etiquetas en un formato de cuadrícula de 3 columnas y 11 filas por página, con cada etiqueta mostrando el modelo, el color, el código de barras, y la talla.

## Notas Importantes

- **Formato del Identificador**: Si el identificador del producto no tiene el formato esperado (`FBAJV1003-NEGRO42`), se omitirá y se mostrará un mensaje de error en la consola.
- **Código de Barras**: Si el código de barras no tiene exactamente 13 dígitos, ese registro también será omitido.
- **Archivos Temporales**: El código genera archivos de imagen temporales para los códigos de barras que luego se eliminan automáticamente una vez que se han añadido al PDF.

## Posibles Problemas y Soluciones

- **Archivo No Encontrado**: Si el archivo Excel no se encuentra, asegúrate de que el nombre y la ubicación sean correctos.
- **Errores de Formato**: Revisa que los identificadores y los códigos de barras cumplan con los formatos requeridos para evitar que se omitan filas.

## Personalización del Código

- **Ubicación del PDF**: Puedes cambiar la ubicación del archivo PDF modificando la variable `pdf_path`.
- **Distribución en la Página**: Si deseas modificar la cantidad de etiquetas por página o la posición de éstas, ajusta las variables `columns`, `rows`, `x_start`, `y_start`, `x_offset`, y `y_offset`.

## Directorios Necesarios

- **Carpeta de Etiquetas**: Asegúrate de que exista una carpeta llamada `etiquetas` en el mismo directorio que el script, o créala manualmente para almacenar el archivo PDF resultante.

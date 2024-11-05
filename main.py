import pandas as pd
import re
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from barcode import EAN13
from barcode.writer import ImageWriter
import os

# Cargar datos del archivo Excel
excel_path = 'PEDIDO CON CODIGOS DE BARRAS.xlsx'
data = pd.read_excel(excel_path)

# Eliminar filas con NaN en las columnas relevantes
data = data.dropna(subset=['identificador_del_producto', 'CODIGO DE BARRAS'])

# Configurar el nombre del archivo de salida
pdf_path = 'etiquetas/etiquetas_zapatos.pdf'
c = canvas.Canvas(pdf_path, pagesize=A4)
width, height = A4

# Configuración de la cuadrícula
columns = 3
rows = 11
x_start = 30  # Margen izquierdo
y_start = height - 30  # Margen superior
x_offset = 200  # Espacio entre columnas
y_offset = 75  # Espacio entre filas

# Recorrer los datos y agregar cada etiqueta al PDF en formato de cuadrícula
col = 0
row = 0
for index, row_data in data.iterrows():
    # Extraer datos del identificador del producto utilizando una expresión regular
    identificador = str(row_data['identificador_del_producto'])
    match = re.match(r"^[A-Z]+([A-Za-z0-9]+)-([A-Za-z]+)(\d+)$", identificador)
    if match:
        modelo = match.group(1)  # Parte del modelo
        color = match.group(2)   # Parte del color
        talla = match.group(3)   # Parte de la talla
    else:
        print(f"Error: El formato del identificador '{identificador}' no es válido.")
        continue

    # Obtener el código de barras
    codigo_barras = str(int(row_data['CODIGO DE BARRAS']))  # Convertir a entero y luego a string

    # Verificar que el código de barras tenga exactamente 13 dígitos
    if len(codigo_barras) != 13:
        print(f"Error: El código de barras {codigo_barras} no tiene 13 dígitos y será omitido.")
        continue

    # Coordenadas para la celda actual
    x = x_start + col * x_offset
    y = y_start - row * y_offset

    # Dibujar el modelo alineado a la izquierda y el color cercano a la derecha del modelo
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x, y, modelo)  # Modelo a la izquierda
    c.drawString(x + 50, y, color)  # Color cercano al modelo

    # Generar el código de barras como imagen y verificar que se guarda correctamente
    barcode_image_path = f"barcode_{codigo_barras}"  # No incluir .png en el nombre
    ean = EAN13(codigo_barras, writer=ImageWriter())
    ean.save(barcode_image_path)  # La función save añadirá automáticamente .png

    # Añadir .png a la ruta para abrirla después de guardarla
    barcode_image_path += ".png"

    # Verificar que la imagen existe antes de intentar dibujarla en el PDF
    if os.path.exists(barcode_image_path):
        # Colocar el código de barras en el PDF, centrado debajo del texto
        c.drawImage(barcode_image_path, x -15 , y - 50, width=45*mm, height=17*mm)

        # Colocar la talla a la derecha del código de barras y alineada verticalmente con este
        c.setFont("Helvetica-Bold", 40)
        c.drawString(x + 100, y - 50 + 16, talla)  # Alinear la talla con la base del código de barras
    else:
        print(f"Error: No se pudo generar la imagen para el código de barras {codigo_barras}")

    # Borrar la imagen temporal del código de barras
    os.remove(barcode_image_path)

    # Mover a la siguiente celda en la cuadrícula
    col += 1
    if col >= columns:
        col = 0
        row += 1
    if row >= rows:
        c.showPage()
        col = 0
        row = 0

# Guardar y cerrar el PDF
c.save()
print(f"PDF creado en: {pdf_path}")

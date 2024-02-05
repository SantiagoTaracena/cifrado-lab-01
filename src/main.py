"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 1 - Encriptado y Decriptado
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el desarrollo del laboratorio.
import sys
from prettytable import PrettyTable

# Módulos necesarios para el desarrollo del laboratorio.
from utils.clean_up_text import clean_up_text
from utils.caesar import encrypt_caesar, decrypt_caesar
from utils.affine import encrypt_affine, decrypt_affine
from utils.vigenere import encrypt_vigenere, decrypt_vigenere
from utils.frequency_analysis import frequency_analysis
from utils.constants.official_frequency_analysis import official_frequency_analysis

# Cantidad de argumentos a pasar al programa.
ARGUMENTS: int = 4

# Paths constantes para los archivos de salida.
ENCRYPTED_OUTPUT_PATH: str = "./out/encrypted-output.txt"
DECRYPTED_OUTPUT_PATH: str = "./out/decrypted-output.txt"

# Verificación del uso correcto de archivos.
if (len(sys.argv) != ARGUMENTS):
    print(f"\nUsage: python {sys.argv[0]} <input-file>.txt <mode> <key>\n")
    sys.exit(1)

# Texto a codificar y método a utilizar.
text: str = open(sys.argv[1], "r", encoding="utf-8").read()
method: str = sys.argv[2]

# Limpieza del texto ingresado.
clean_text: str = clean_up_text(text)

# Verificación del método a utilizar siendo el método de César.
if (method == "caesar"):

    # Llave a utilizar, es decir, traslación de cada caracter.
    try:
        key: int = int(sys.argv[3])

    # Verificación de errores al convertir a int.
    except ValueError:
        print(f"\nUsage: python {sys.argv[0]} <input-file>.txt caesar <key: integer>\n")
        sys.exit(1)

    # Encriptación del texto por el método de cifrado de César.
    encrypted_text: str = encrypt_caesar(clean_text, key)

    # Escritura del texto encriptado resultante en un archivo.
    with open(ENCRYPTED_OUTPUT_PATH, "w", encoding="utf-8") as file:
        file.write(encrypted_text)

    # Decriptación del texto por el método de cifrado de César.
    decrypted_text: str = decrypt_caesar(encrypted_text, key)

    # Escritura del texto decriptado resultante en un archivo.
    with open(DECRYPTED_OUTPUT_PATH, "w", encoding="utf-8") as file:
        file.write(decrypted_text)

    # Impresión de los resultados.
    print(f"\nTexto original: {text}\n\nTexto limpio y encriptado: {encrypted_text}\n\nTexto decriptado: {decrypted_text}\n")

# Verificación del método a utilizar siendo el método de Afines.
elif (method == "affine"):

    # Llave inicial obtenida de la separación del argumento dado.
    key: list[str] = sys.argv[3].split(",")

    # Verificación de que la llave tenga los argumentos a y b necesarios.
    if (len(key) != 2):
        print(f"\nUsage: python {sys.argv[0]} <input-file>.txt affine <a: integer, b: integer>\n")
        sys.exit(1)

    # Conversión a números de las llaves a utilizar.
    try:
        a: int = int(key[0])
        b: int = int(key[1])

    # Verificación de errores al convertir a int.
    except ValueError:
        print(f"\nUsage: python {sys.argv[0]} <input-file>.txt affine <a: integer, b: integer>\n")
        sys.exit(1)

    # Encriptación del texto por el método de cifrado de Afines.
    encrypted_text: str = encrypt_affine(clean_text, a, b)

    # Escritura del texto encriptado resultante en un archivo.
    with open(ENCRYPTED_OUTPUT_PATH, "w", encoding="utf-8") as file:
        file.write(encrypted_text)

    # Decriptación del texto por el método de cifrado de Afines.
    decrypted_text: str = decrypt_affine(encrypted_text, a, b)

    # Escritura del texto decriptado resultante en un archivo.
    with open(DECRYPTED_OUTPUT_PATH, "w", encoding="utf-8") as file:
        file.write(decrypted_text)

    # Impresión de los resultados.
    print(f"\nTexto original: {text}\n\nTexto limpio y encriptado: {encrypted_text}\n\nTexto decriptado: {decrypted_text}\n")

# Verificación del método a utilizar siendo el método de Vigenére.
elif (method == "vigenere"):

    # Obtención de la llave a utilizar por el método.
    key: str = sys.argv[3].lower()

    # Encriptación del texto por el método de cifrado de Vigenére.
    encrypted_text: str = encrypt_vigenere(clean_text, key)

    # Escritura del texto encriptado resultante en un archivo.
    with open(ENCRYPTED_OUTPUT_PATH, "w", encoding="utf-8") as file:
        file.write(encrypted_text)

    # Decriptación del texto por el método de cifrado de Vigenére.
    decrypted_text = decrypt_vigenere(encrypted_text, key)

    # Escritura del texto decriptado resultante en un archivo.
    with open(DECRYPTED_OUTPUT_PATH, "w", encoding="utf-8") as file:
        file.write(decrypted_text)

    # Impresión de los resultados.
    print(f"\nTexto original: {text}\n\nTexto limpio y encriptado: {encrypted_text}\n\nTexto decriptado: {decrypted_text}\n")

# Caso en el que el método de encriptado sea incorrecto.
else:
    print(f"\nUsage: python {sys.argv[0]} <input-file>.txt <caesar | affine | vigenere> <key>\n")
    sys.exit(1)

# Tabla para observar los resultados del análisis de frecuencia.
frequency_analysis_table: PrettyTable = PrettyTable()

# Definición de las columnas de la tabla.
frequency_analysis_table.field_names = ["Letra", "Análisis", "Oficial"]

# Análisis de frecuencia realizado al texto encriptado.
frequency_analysis_result: dict[str, float] = frequency_analysis(encrypted_text)

# Agregación de filas para cada caracter.
for char in frequency_analysis_result:
    frequency_analysis_table.add_row([char, frequency_analysis_result[char], official_frequency_analysis[char]])

# Impresión de la tabla final.
print(frequency_analysis_table, "\n")

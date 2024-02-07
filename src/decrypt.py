"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 1 - Encriptado y Decriptado
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el desarrollo del laboratorio.
import sys

# Módulos necesarios para el desarrollo del laboratorio.
from utils.clean_up_text import clean_up_text
from utils.frequency_analysis import frequency_analysis
from utils.caesar_brute_force import caesar_brute_force
from utils.affine_brute_force import affine_brute_force
from utils.vigenere_brute_force import vigenere_brute_force

# Módulos necesarios para el desarrollo del laboratorio.
ARGUMENTS: int = 3

# Verificación del uso correcto de archivos.
if (len(sys.argv) != ARGUMENTS):
    print(f"\nUsage: python {sys.argv[0]} <input-file>.txt <mode>\n")
    sys.exit(1)

# Texto a decriptar y método a utilizar.
encrypted_text: str = open(sys.argv[1], "r", encoding="utf-8").read()
method: str = sys.argv[2]

# Limpieza del texto ingresado.
clean_encrypted_text: str = clean_up_text(encrypted_text)

# Análisis de frecuencia del texto encriptado.
frequency_analysis_result: dict[str, float] = frequency_analysis(clean_encrypted_text)

# Verificación de que el método a utilizar sea el método de César.
if (method == "caesar"):

    # Búsqueda mediante el método de fuerza bruta para descifrar un texto con el método de César.
    caesar_brute_force(clean_encrypted_text, frequency_analysis_result)

# Verificación de que el método a utilizar sea el método de Afines.
elif (method == "affine"):

    # Búsqueda mediante el método de fuerza bruta para descifrar un texto con el método de Afines.
    affine_brute_force(clean_encrypted_text, a_val_range=(22, 24), b_val_range=(5, 10))

# Verificación de que el método a utilizar sea el método de Vigenére.
elif (method == "vigenere"):

    # Búsqueda mediante el método de fuerza bruta para descifrar un texto con el método de Vigenére.
    vigenere_brute_force(clean_encrypted_text, key_lenght=4)

# Caso en el que el método de decriptado sea incorrecto.
else:
    print(f"\nUsage: python {sys.argv[0]} <input-file>.txt <caesar | affine | vigenere>\n")
    sys.exit(1)

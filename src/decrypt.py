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

frequency_analysis_result: dict[str, float] = frequency_analysis(clean_encrypted_text)

if (method == "caesar"):

    caesar_brute_force(clean_encrypted_text, frequency_analysis_result)

elif (method == "affine"):

    affine_brute_force(clean_encrypted_text, (22, 24), (5, 9))

elif (method == "vigenere"):

    ...

# Caso en el que el método de decriptado sea incorrecto.
else:
    print(f"\nUsage: python {sys.argv[0]} <input-file>.txt <caesar | affine | vigenere>\n")
    sys.exit(1)

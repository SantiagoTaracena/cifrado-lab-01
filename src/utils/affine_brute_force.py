"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 1 - Encriptado y Decriptado
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para el desarrollo del método de fuerza bruta.
from utils.clean_up_text import clean_up_text
from utils.affine import decrypt_affine

# Función affine_brute_force, que prueba a fuerza bruta desencriptar un texto cifrado con Afines.
def affine_brute_force(encrypted_text, a_val_range: tuple[int], b_val_range: tuple[int]):

    # Limpieza del texto encriptado inicial.
    encrypted_text: str = clean_up_text(encrypted_text)

    # Valores mínimos y máximos de a y b.
    a_min, a_max = a_val_range
    b_min, b_max = b_val_range

    # Ciclos que realizan las pruebas de los valores a probar para descifrar el texto.
    for a in range(a_min, a_max):
        for b in range(b_min, b_max):
            print("Probando el valor a", a, "y el valor b", b, "el resultado es:\n", decrypt_affine(encrypted_text, a, b))

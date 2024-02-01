"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 1 - Encriptado y Decriptado
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para el desarrollo del método de fuerza bruta.
from utils.clean_up_text import clean_up_text
from utils.caesar import decrypt_caesar
from utils.constants.alphabet import alphabet

# Función caesar_brute_force, que prueba a fuerza bruta desencriptar un texto cifrado con César.
def caesar_brute_force(encrypted_text: str, frequency_analysis: dict[str, float]) -> None:

    # Limpieza del texto encriptado inicial.
    encrypted_text: str = clean_up_text(encrypted_text)

    # Letra con la máxima frecuencia del análisis y desplazamiento calculado.
    max_letter: str = max(frequency_analysis.items(), key=lambda item: item[1])[0]
    displacement: int = alphabet.index(max_letter) - alphabet.index("e")

    # Cambio del desplazamiento a positivo si este es negativo.
    if (displacement < 0):
        displacement = len(alphabet) + displacement

    # Ciclo que prueba todas las llaves necesarias para decifrar el texto.
    for _ in range(len(alphabet)):
        key_to_test: int = displacement % len(alphabet)
        displacement += 1
        print("Probando la llave", key_to_test, "el resultado es:\n", decrypt_caesar(encrypted_text, key_to_test), "\n")

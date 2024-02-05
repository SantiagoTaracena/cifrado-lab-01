"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 1 - Encriptado y Decriptado
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para el desarrollo del método de fuerza bruta.
from utils.clean_up_text import clean_up_text
from utils.caesar import decrypt_caesar
from utils.text_entropy import text_entropy
from utils.constants.alphabet import alphabet

# Función caesar_brute_force, que prueba a fuerza bruta desencriptar un texto cifrado con César.
def caesar_brute_force(encrypted_text: str, frequency_analysis: dict[str, float]) -> None:

    # Resultados de la decriptación.
    decryption_results: dict[int, str] = dict()
    decryption_entropy_results: dict[int, float] = dict()

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

        # Llave, texto decriptado y entropía encontrada.
        key_to_test: int = displacement % len(alphabet)
        decrypted_text_tested: str = decrypt_caesar(encrypted_text, key_to_test)
        decrypted_text_tested_entropy: float = text_entropy(decrypted_text_tested)

        # Almacenamiento de los resultados.
        decryption_results[key_to_test] = decrypted_text_tested
        decryption_entropy_results[key_to_test] = decrypted_text_tested_entropy
        displacement += 1

    # Ordenamiento de los resultados según la entropía hallada.
    sorted_results: dict[int, float] = dict(sorted(decryption_entropy_results.items(), key=lambda item: item[1]))
    sorted_keys: list[int] = list(sorted_results.keys())

    # Escritura de los resultados obtenidos.
    with open("./out/brute-force-decryption-results.txt", "w", encoding="utf-8") as file:
        for key in sorted_keys:
            file.write(f"key {key}: {decryption_results[key]}\n\n")

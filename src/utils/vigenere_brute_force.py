"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 1 - Encriptado y Decriptado
Santiago Taracena Puga (20017)
"""

# Librerías necesarias para el desarrollo del método de fuerza bruta.
from itertools import product

# Módulos necesarios para el desarrollo del método de fuerza bruta.
from utils.clean_up_text import clean_up_text
from utils.vigenere import decrypt_vigenere
from utils.text_entropy import text_entropy

# Función para generar las llaves a utilizar.
def generate_permutations(n: int) -> list[str]:
    alphabet = "abcdefghijklmnñopqrstuvwxyz"
    permutations = product(alphabet, repeat=n)
    permutation_list = ["".join(permutation) for permutation in permutations]
    return permutation_list

# Función vigenere_brute_force, que prueba a fuerza bruta desencriptar un texto cifrado con Vigenére.
def vigenere_brute_force(encrypted_text: str, key_lenght: int) -> None:

    # Resultados de la decriptación.
    decryption_results: dict[int, str] = dict()
    decryption_entropy_results: dict[int, float] = dict()

    # Limpieza del texto encriptado inicial.
    encrypted_text: str = clean_up_text(encrypted_text)

    # Posibles llaves a utilizar con la longitud dada.
    possible_keys: list[str] = generate_permutations(key_lenght)

    # Ciclo que prueba todas las llaves a utilizar.
    for key in possible_keys:

        # Llave, texto decriptado y entropía encontrada.
        decrypted_text_tested: str = decrypt_vigenere(encrypted_text, key)
        decrypted_text_tested_entropy: float = text_entropy(decrypted_text_tested)

        # Almacenamiento de los resultados.
        decryption_results[key] = decrypted_text_tested
        decryption_entropy_results[key] = decrypted_text_tested_entropy

    # Ordenamiento de los resultados según la entropía hallada.
    sorted_results: dict[int, float] = dict(sorted(decryption_entropy_results.items(), key=lambda item: item[1]))
    sorted_keys: list[int] = list(sorted_results.keys())

    # Escritura de los resultados obtenidos.
    with open("./out/brute-force-decryption-results.txt", "w", encoding="utf-8") as file:
        for key in sorted_keys:
            file.write(f"key {key}: {decryption_results[key]}\n\n")

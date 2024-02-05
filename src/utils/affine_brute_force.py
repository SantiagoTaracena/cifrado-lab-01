"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 1 - Encriptado y Decriptado
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para el desarrollo del método de fuerza bruta.
from utils.clean_up_text import clean_up_text
from utils.affine import decrypt_affine
from utils.text_entropy import text_entropy

# Función affine_brute_force, que prueba a fuerza bruta desencriptar un texto cifrado con Afines.
def affine_brute_force(encrypted_text, a_val_range: tuple[int], b_val_range: tuple[int]):

    # Resultados de la decriptación.
    decryption_results: dict[int, str] = dict()
    decryption_entropy_results: dict[int, float] = dict()

    # Limpieza del texto encriptado inicial.
    encrypted_text: str = clean_up_text(encrypted_text)

    # Valores mínimos y máximos de a y b.
    a_min, a_max = a_val_range
    b_min, b_max = b_val_range

    # Ciclos que realizan las pruebas de los valores a probar para descifrar el texto.
    for a in range(a_min, a_max):
        for b in range(b_min, b_max):

            # Llave, texto decriptado y entropía encontrada.
            a_b_key_to_test: str = f"{a},{b}"
            decrypted_text_tested: str = decrypt_affine(encrypted_text, a, b)
            decrypted_text_tested_entropy: float = text_entropy(decrypted_text_tested)

            # Almacenamiento de los resultados.
            decryption_results[a_b_key_to_test] = decrypted_text_tested
            decryption_entropy_results[a_b_key_to_test] = decrypted_text_tested_entropy

    # Ordenamiento de los resultados según la entropía hallada.
    sorted_results: dict[int, float] = dict(sorted(decryption_entropy_results.items(), key=lambda item: item[1]))
    sorted_keys: list[int] = list(sorted_results.keys())

    # Escritura de los resultados obtenidos.
    with open("./out/brute-force-decryption-results.txt", "w", encoding="utf-8") as file:
        for key in sorted_keys:
            file.write(f"key {key}: {decryption_results[key]}\n\n")


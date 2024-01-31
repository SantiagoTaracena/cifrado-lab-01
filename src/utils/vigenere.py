"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 1 - Encriptado y Decriptado
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para el desarrollo de las funciones de Vigenére.
from utils.constants.alphabet import alphabet
from utils.constants.vigenere_cipher_matrix import vigenere_cipher_matrix

# Función encrypt_vigenere, que encripta un texto por cifrado de Vigenére.
def encrypt_vigenere(text: str, key: str) -> str:

    # Llave para cifrar el texto por el cifrado de Vigenére.
    cipher_key: str = (key * (len(text) // len(key))) + key[:len(text) % len(key)]

    # Instancia del texto encriptado inicial.
    encrypted_text: str = str()

    # Ciclo que itera a través del texto y la llave a utilizar.
    for text_char, key_char in zip(text, cipher_key):

        # Verificación de que el caracter esté en el alfabeto.
        if (text_char in alphabet):

            # Índice y obtención de la fila a utilizar para cifrar el caracter dado.
            alphabet_index: int = alphabet.index(text_char)
            vigenere_cipher_matrix_row: list[str] = vigenere_cipher_matrix[alphabet_index]

            # Índice y obtención del caracter cifrado dado el caracter original del texto.
            cipher_key_index: int = alphabet.index(key_char)
            vigenere_cipher_matrix_char: str = vigenere_cipher_matrix_row[cipher_key_index]

            # Agregación del caracter encriptado al texto.
            encrypted_text += vigenere_cipher_matrix_char

        # Si el caracter no está en el alfabeto, no se encripta.
        else:

            # Agregación del caracter sin encriptar al texto.
            encrypted_text += text_char

    # Retorno del texto encriptado.
    return encrypted_text

# Función decrypt_vigenere, que decripta un texto cifrado por el método de Vigenére.
def decrypt_vigenere(encrypted_text: str, key: str) -> str:

    # Llave para descifrar el texto por el cifrado de Vigenére.
    cipher_key: str = (key * (len(encrypted_text) // len(key))) + key[:len(encrypted_text) % len(key)]

    # Instancia del texto decriptado inicial.
    decrypted_text: str = str()

    # Ciclo que itera a través de los caracteres del texto encriptado y la llave.
    for encrypted_char, key_char in zip(encrypted_text, cipher_key):

        # Verificación de que el caracter esté en el alfabeto.
        if (encrypted_char in alphabet):

            # Índice y obtención de la columna para decriptar el caracter obtenido.
            column_index: int = vigenere_cipher_matrix[0].index(key_char)
            column_to_search: list[str] = [row[column_index] for row in vigenere_cipher_matrix]

            # Índice y obtención del caracter decriptado.
            decrypted_char_position: int = column_to_search.index(encrypted_char)
            decrypted_char: str = vigenere_cipher_matrix[decrypted_char_position][0]

            # Agregación del caracter decriptado al texto.
            decrypted_text += decrypted_char

        # Si el caracter no está en el alfabeto, no se decripta.
        else:

            # Agregación del caracter sin decriptar al texto.
            decrypted_text += encrypted_char

    # Retorno del texto decriptado.
    return decrypted_text

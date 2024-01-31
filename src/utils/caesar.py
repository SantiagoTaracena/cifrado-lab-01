"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 1 - Encriptado y Decriptado
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para el desarrollo de las funciones de César.
from utils.constants.alphabet import alphabet

# Función encrypt_caesar, que encripta un texto por cifrado de César.
def encrypt_caesar(text: str, key: str) -> str:

    # Instancia del texto encriptado inicial.
    encrypted_text: str = str()

    # Ciclo que itera a través de los caracteres del texto.
    for char in text:

        # Verificación de que el caracter esté en el alfabeto.
        if (char in alphabet):

            # Caracter encriptado y agregación al texto encriptado completo.
            encrypted_char: str = alphabet[(alphabet.index(char) + key) % len(alphabet)]
            encrypted_text += encrypted_char

        # Si el caracter no está en el alfabeto, no se encripta.
        else:

            # Agregación del caracter sin encriptar al texto.
            encrypted_text += char

    # Retorno del texto encriptado.
    return encrypted_text

# Función decrypt_caesar, que decripta un texto cifrado por método de cifrado de César.
def decrypt_caesar(encrypted_text: str, key: str) -> str:

    # Instancia del texto decriptado inicial.
    decrypted_text: str = str()

    # Ciclo que itera a través de los caracteres del texto encriptado.
    for encrypted_char in encrypted_text:

        # Verificación de que el caracter esté en el alfabeto.
        if (encrypted_char in alphabet):

            # Caracter decriptado y agregación al texto decriptado completo.
            char: str = alphabet[(alphabet.index(encrypted_char) - key) % len(alphabet)]
            decrypted_text += char

        # Si el caracter no está en el alfabeto, no se decripta.
        else:

            # Agregación del caracter sin decriptar al texto.
            decrypted_text += encrypted_char

    # Retorno del texto decriptado.
    return decrypted_text

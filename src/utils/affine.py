"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 1 - Encriptado y Decriptado
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para el desarrollo de las funciones de cifrado de Afines.
from utils.constants.alphabet import alphabet

# Función extended_euclides para obtener el MCD por el método de Euclides.
def extended_euclides(a: int, b: int) -> tuple[int]:

    # Si a es cero, se retorna el MCD igual a b, 0 y 1.
    if (a == 0):
        return (b, 0, 1)

    # Para cualquier otro caso se obtiene el MCD de forma recursiva.
    else:

        # Obtención del MCD y retorno del resultado del algoritmo.
        mcd, x, y = extended_euclides(b % a, a)
        return (mcd, y - (b // a) * x, x)

# Función get_inverse_a_value para obtener el valor inverso de a para decriptar el método.
def get_inverse_a_value(a: int, m: int) -> int:

    # MCD y valor del inverso de a obtenido.
    mcd, x, _ = extended_euclides(a, m)

    # Si el MCD es 1, se retorna el inverso obtenido.
    if (mcd == 1):

        # Retorno del inverso multiplicativo
        return (x % m)

    # En cualquier otro caso, no hay inverso multiplicativo.
    return 0

# Función encrypt_affine, que encripta un mensaje mediante cifrado de Afines.
def encrypt_affine(text: str, a: int, b: int) -> str:

    # Instancia del texto encriptado inicial.
    encrypted_text: str = str()

    # Ciclo que itera a través de los caracteres del texto.
    for char in text:

        # Verificación de que el caracter esté en el alfabeto.
        if (char in alphabet):

            # Caracter encriptado y agregación al texto encriptado completo.
            encrypted_char: str = alphabet[((a * alphabet.index(char)) + b) % len(alphabet)]
            encrypted_text += encrypted_char

        # Si el caracter no está en el alfabeto, no se encripta.
        else:

            # Agregación del caracter sin encriptar al texto.
            encrypted_text += char

    # Retorno del texto encriptado.
    return encrypted_text

# Función decrypt_affine, que decripta un mensaje que ha sido encriptado mediante cifrado de Afines.
def decrypt_affine(encrypted_text: str, a: int, b: int) -> str:

    # Inverso multiplicativo del valor de a.
    inverse_a_value: int = get_inverse_a_value(a, len(alphabet))

    # Instancia del texto decriptado inicial.
    decrypted_text: str = str()

    # Ciclo que itera a través de los caracteres del texto encriptado.
    for encrypted_char in encrypted_text:

        # Verificación de que el caracter esté en el alfabeto.
        if (encrypted_char in alphabet):

            # Caracter decriptado y agregación al texto decriptado completo.
            decrypted_char: str = alphabet[(inverse_a_value * (alphabet.index(encrypted_char) - b)) % len(alphabet)]
            decrypted_text += decrypted_char

        # Si el caracter no está en el alfabeto, no se decripta.
        else:

            # Agregación del caracter sin decriptar al texto.
            decrypted_text += encrypted_char

    # Retorno del texto decriptado.
    return decrypted_text

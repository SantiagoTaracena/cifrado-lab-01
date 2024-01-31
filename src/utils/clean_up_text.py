"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 1 - Encriptado y Decriptado
Santiago Taracena Puga (20017)
"""

# Librería unidecode para remover tildes.
import unidecode

# Definición de la función clean_up_text para limpiar texto.
def clean_up_text(text: str) -> str:

    # Palabras pertenecientes al texto y lista para guardar el texto limpio.
    text_words: list[str] = text.split(" ")
    clean_text_list: list[str] = []

    # Ciclo que itera las palabras del texto.
    for word in text_words:

        # Lista para guardar las palabras del texto ya limpio.
        clean_word_list: list[str] = []

        # Ciclo que itera los caracteres de cada palabra.
        for char in word:

            # Si el caracter pertenece al alfabeto definido.
            if (char.isalpha()):

                # El caracter se pasa a lower y se agrega a las palabras.
                clean_word_list.append(char.lower())

            # Cualquier otro caso, es decir, símbolos.
            else:

                # El caracter no necesita limpiarse.
                clean_word_list.append(char)

        # Palabra limpia de tildes.
        clean_word: str = unidecode.unidecode("".join(clean_word_list))

        # Agregación de la palabra limpia a la lista de palabras limpias.
        clean_text_list.append(clean_word)

    # Texto limpio obtenido de la unión de palabras listas.
    clean_text: str = " ".join(clean_text_list)

    # Retorno del texto limpio.
    return clean_text

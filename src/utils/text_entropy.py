"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 1 - Encriptado y Decriptado
Santiago Taracena Puga (20017)
"""

# Librería necesaria para la obtención de la entropía del texto.
import math

# Módulo necesario para la obtención de la entropía del texto.
from utils.constants.official_frequency_analysis import official_frequency_analysis

# Función que obtiene la entropía de un texto.
def text_entropy(text: str) -> float:

    # Limpieza y conversión del texto a minúsculas.
    text: str = text.lower()

    # Probabilidades de cada letra del texto.
    local_probabilities: list[float] = [(text.count(char) / len(text)) for char in set(text)]
    global_probabilities: list[float] = [(official_frequency_analysis.get(char, 0.0001)) for char in set(text)]

    # Obtención de la entropía total del texto.
    text_entropy_value: float = sum([(probability * math.log2(probability / q_probability)) for probability, q_probability in zip(local_probabilities, global_probabilities)])

    # Retorno de la entropía total del texto.
    return text_entropy_value

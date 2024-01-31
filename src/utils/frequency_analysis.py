"""
Universidad del Valle de Guatemala
(CC3078) Cifrado de Información
Laboratorio 1 - Encriptado y Decriptado
Santiago Taracena Puga (20017)
"""

# Módulos necesarios para el desarrollo del laboratorio.
from utils.constants.alphabet import alphabet

# Función frequency_analysis, que obtiene el análisis de frecuencias de un texto encriptado.
def frequency_analysis(encrypted_text: str) -> dict[str, float]:

    # Instancia del análisis de frecuencias inicial.
    frequency_analysis_result: dict[str, int] = { char: 0 for char in alphabet }

    # Obtención de la probabilidad dada.
    for char in encrypted_text:
        if char in alphabet:
            frequency_analysis_result[char] += 1

    # Retorno del análisis de frecuencias.
    return { char: round(frequency_analysis_result[char] / len(encrypted_text), 3) for char in alphabet }

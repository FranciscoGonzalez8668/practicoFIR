import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

def goertzel(samples, sample_rate, target_freq):
    """
    Algoritmo de Goertzel para detectar una frecuencia específica.
    samples: Señal de entrada (array de muestras)
    sample_rate: Frecuencia de muestreo de la señal (Hz)
    target_freq: Frecuencia objetivo a detectar (Hz)
    """
    N = len(samples)  # Número de muestras
    k = int(0.5 + (N * target_freq) / sample_rate)  # Índice para la frecuencia objetivo

    # Coeficiente de realimentación
    w = 2.0 * np.pi * k / N
    cosine = np.cos(w)
    coeff = 2.0 * cosine

    # Inicialización de variables
    s_prev = 0.0
    s_prev2 = 0.0

    # Fase de acumulación
    for sample in samples:
        s = sample + coeff * s_prev - s_prev2
        s_prev2 = s_prev
        s_prev = s

    # Cálculo de la energía detectada
    power = s_prev2**2 + s_prev**2 - coeff * s_prev * s_prev2
    return power

# Cargar el archivo WAV
sample_rate, data = wavfile.read("robot_36.48k.wav")  # Reemplazar con tu archivo WAV

# Si es estéreo, tomar solo un canal
if len(data.shape) > 1:
    data = data[:, 0]

# Definir el rango de frecuencias a analizar
start_freq = 1000  # Frecuencia mínima (Hz)
end_freq = 2800   # Frecuencia máxima (Hz)
step = 10  # Intervalo entre frecuencias a analizar

# Detectar energías en el rango de frecuencias
frequencies = np.arange(start_freq, end_freq, step)
powers = [goertzel(data, sample_rate, freq) for freq in frequencies]

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(frequencies, powers, marker='o')
plt.title("Energía detectada por frecuencia")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Energía")
plt.grid(True)
plt.show()

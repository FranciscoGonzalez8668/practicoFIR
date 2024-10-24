import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Frecuencia de muestreo (en Hz)
fs = 10000

# Frecuencia de corte (en Hz)
f1 = 1500  # Frecuencia baja (0V)
f2 = 2500  # Frecuencia alta (1V)

# Frecuencias normalizadas (dividir entre fs/2)
frequencies = [0, f1/(fs/2), f2/(fs/2), 1]

# Ganancias deseadas en cada banda (0 para f1, 1 para f2)
gains = [0, 0, 1, 1]

# Número de coeficientes (orden del filtro FIR)
num_taps = 101

# Calcular los coeficientes del filtro FIR
fir_coefficients = signal.firwin2(num_taps, frequencies, gains)

with open('fir_taps.txt', 'w') as f:
    # Convertir los coeficientes a cadena separada por comas y escribir en el archivo
    f.write(','.join(map(str, fir_coefficients)))


# Visualizar la respuesta en frecuencia
w, h = signal.freqz(fir_coefficients, worN=8000)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.title("Respuesta en frecuencia del filtro FIR")
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.grid()
plt.show()

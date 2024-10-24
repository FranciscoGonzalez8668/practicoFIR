from scipy.signal import firwin, freqz
import matplotlib.pyplot as plt
import numpy as np

# Parámetros del filtro
fs = 22050  # Frecuencia de muestreo (Hz)
cutoff = [1500, 2300]  # Frecuencias de corte (Hz)
numtaps = 101  # Número de coeficientes del filtro (longitud FIR)

# Diseño del filtro de banda eliminada
fir_coeff = firwin(numtaps, cutoff, fs=fs, pass_zero=True)

# Frecuencia de respuesta
w, h = freqz(fir_coeff, worN=8000)

# Guardar los coeficientes en un archivo .txt
with open('fir_taps.txt', 'w') as f:
    f.write(','.join(map(str, fir_coeff)))


# Gráfico de la respuesta del filtro
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.title('Respuesta de Frecuencia del Filtro FIR')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Ganancia')
plt.grid()
plt.show()

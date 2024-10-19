import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Parámetros de diseño
fs = 48000  # Frecuencia de muestreo en Hz
numtaps = 101  # Número de coeficientes (orden del filtro)
lowcut = 1500.0  # Frecuencia inferior de la banda eliminada
highcut = 2300.0  # Frecuencia superior de la banda eliminada

# Diseño del filtro FIR de banda eliminada
filtro = firwin(numtaps, [lowcut, highcut], pass_zero=True, fs=fs)

#Guardar los coeficientes del filtro en archivo.txt 
with open('coeficientes_filtro_FIR.txt', 'w') as f:
    # Crear una cadena de texto con los coeficientes separados por comas
    coef_string = ', '.join(f'{coef:.10f}' for coef in filtro)
    # Escribir la cadena en el archivo
    f.write(coef_string)

# Graficar la respuesta en frecuencia del filtro
w, h = freqz(filtro, fs=fs)
plt.plot(w, 20 * np.log10(abs(h)))
plt.title('Respuesta en frecuencia del filtro FIR de banda eliminada (1500-2300 Hz)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud (dB)')
plt.grid()
plt.show()

# Si deseas aplicar el filtro a una señal (ejemplo):
from scipy.signal import lfilter

# Generar una señal de prueba con componentes de 1500 Hz y 2300 Hz
t = np.arange(0, 1.0, 1/fs)
signal = np.sin(2 * np.pi * 1600 * t) + np.sin(2 * np.pi * 2200 * t)

# Filtrar la señal
signal_filtrada = lfilter(filtro, 1.0, signal)

# Graficar la señal original y la señal filtrada
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Señal original (con 1500 y 2300 Hz)')
plt.subplot(2, 1, 2)
plt.plot(t, signal_filtrada)
plt.title('Señal filtrada (sin componentes entre 1500 y 2300 Hz)')
plt.show()
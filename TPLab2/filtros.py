
import numpy as np
import scipy.signal as sp
from matplotlib import pyplot as plt

from pytc2.sistemas_lineales import plot_plantilla

## FILTRO NOTCH IIR

b1,a1 = sp.iirdesign([0.098, 0.102], [0.0999, 0.1001], 3, 60, ftype='butter')
sos1 = sp.iirdesign([0.098, 0.102], [0.0999, 0.1001], 3, 60, output='sos', ftype='butter')
w1, h1 = sp.freqz(b1,a1, worN=8000)

wf1 = w1/(np.pi)
magnitud_db_1 = 20 * np.log10(np.abs(h1))

plt.figure(figsize=(8, 5))
plt.plot(wf1, magnitud_db_1, 'r', label='Magnitud')
plt.title("Notch")
plt.xlabel('Frecuencia Digital [Omega]')
plt.ylabel('Amplitud [dB]')
plt.grid(True)
plt.legend()
plt.xlim(0,1)
plt.ylim(-100, 5)  # Ajustar límite del eje Y para ver la caída
plt.show()

print("notch iir:")
print("[", end="")

for i in sos1:
    print("[", end="")
    for j in i:
        print(f"{j}, ", end="")
    print("],")
print("]")


## FILTRO PASABAJOS FIR

fc = 0.2
amax = 1
fs = 0.6
amin = 60
N = 101

frecs = [0, fc, fs, 1]
gains = [0, -amax, -amin, -np.inf]
gains = 10**(np.array(gains)/20)

bfir = sp.firwin2(N, frecs, gains , window='hamming')
wfir, hfir = sp.freqz(bfir, 1.0)
wfir = wfir/(np.pi)
magfir = 20 * np.log10(np.abs(hfir))

plt.figure(figsize=(8, 5))
plt.plot(wfir, magfir, 'g', label='Magnitud')
plt.title("PB FIR")
plt.xlabel('Frecuencia Digital [Omega]')
plt.ylabel('Amplitud [dB]')
plt.grid(True)
plt.legend()
plt.xlim(0,1)
plt.ylim(-100, 5)  # Ajustar límite del eje Y para ver la caída
plt.show()

print(f"Orden del filtro FIR = {len(bfir)}")

#Se comenta este bloque para que los 101 coeficientes del filtro no ocupen lugar

#print("lowpass fir:")
#print("[", end="")
#for i in bfir:
#    print(f"{i},", end="")
#print("]")
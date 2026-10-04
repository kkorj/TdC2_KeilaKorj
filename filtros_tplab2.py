#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 23:08:47 2026

@author: keila
"""

import numpy as np
import scipy.signal as sp
from matplotlib import pyplot as plt
from pytc2.sistemas_lineales import plot_plantilla

# --- FILTRO A: PASABAJOS CHEBYSHEV FIR ---
fp = 100     # Hz (frecuencia de paso)
fstop = 300  # Hz (frecuencia de detención)
alfa_max = 1 # dB
alfa_min = 60# dB
fs = 1000    # Hz (frecuencia de muestreo)

# IIR Chebyshev
system_a = sp.iirdesign(fp, fstop, alfa_max, alfa_min, ftype='cheby1', output='sos', fs=fs)
w_iir, h_iir = sp.freqz_sos(system_a, worN=1000, fs=fs)


N = 101
frecs = [0, fp, fstop, fs/2]
gains = [0, -alfa_max, -alfa_min, -np.inf]
gains = 10**(np.array(gains)/20)
bfir = sp.firwin2(N, frecs, gains, window='hamming', fs=fs)
w_fir, h_fir = sp.freqz(bfir, fs=fs)

mag_fir = 20 * np.log10(np.abs(h_fir))

plt.figure()
plt.plot(w_fir,mag_fir)

plt.title('FILTRO PASABAJOS FIR')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [dB]')
plt.grid(which='both', axis='both')

plot_plantilla(filter_type = 'lowpass' , fpass = fp, ripple = alfa_max , fstop = fstop, attenuation = alfa_min, fs = fs)

print(f"Orden del filtro FIR = {len(bfir)}")



# --- FILTRO B: NOTCH IIR ---
fnotch = 50  # Hz
BW = 1       # Hz
fpass = (fnotch - BW/2, fnotch + BW/2)
fstop_b = (fnotch - 0.05, fnotch + 0.05)


system_b = sp.iirdesign(fpass, fstop_b, 3, 60, ftype='butter', output='sos', fs=fs)
w_notch, h_notch = sp.freqz_sos(system_b, worN=10000, fs=fs)

plt.figure()

plt.plot(w_notch,20*np.log10(np.abs(h_notch)+ 1e-12))


plt.title('FILTRO NOTCH IIR')
plt.xlabel('Frecuencia[Hz]')
plt.ylabel('Amplitud [dB]')
plt.grid(which='both', axis='both')

plot_plantilla(filter_type = 'bandstop' , fpass = fpass, ripple = alfa_max , fstop = fstop_b, attenuation = alfa_min, fs = fs)

print(f"Orden Total del filtro Notch IIR = {len(system_b) * 2}") #system_b es una matriz SOS donde cada fila es una sección de 2º orden


import matplotlib.pyplot as plt
from scipy import signal as sig

plt.style.use('seaborn-v0_8-darkgrid')


##########################FILTRO A: PASABAJOS FIR##############################
f = np.array([30,50,70,80,90,100,110,130,150,200,300])
V_in = np.array([2.11,2.20,2.15,2.16,2.16,2.11,2.1,2.07,2.07,2.05,2.05])
V_out = np.array([1.96,1.87,1.75,1.67,1.63,1.60,1.51,1.27,1.08,0.576,0.02])

T = 20 * np.log10(V_out / V_in)

fig, ax1 = plt.subplots()

ax1.plot(w_fir,mag_fir, label='Teórica', linewidth=2)
ax1.plot(f, T, 'o', label='Mediciones', markersize=6, color='#f51414', markeredgecolor='white', markeredgewidth=1)
ax1.set_xlabel('Frecuencia[HZ]', fontsize=12)
ax1.set_ylabel('Magnitud[DB]', fontsize=12)
ax1.set_title('Filtro A: Pasabajos FIR', fontsize=14, fontweight='bold')
ax1.legend(fontsize=11, loc='best')
ax1.grid(True, which='both',color='black', alpha=0.3)
ax1.tick_params(labelsize=10)

ax1.set_xlim([0, 500])

ax1.set_ylim([-50, 5])

plt.tight_layout()
plt.show()

##########################FILTRO B: NOTCH IIR########################
f = np.array([40,45,49,49.2,49.5,49.7,49.9,50,50.2,50.5,50.7,50.9,51,55,60])
V_in = np.array([3.35,3.27,3.27,3.16,3.35,3.24,3.24,3.16,3.11,3.11,3.11,3.03,3.11,3.27,3.31])
V_out = np.array([3.03,2.96,2.24,1.55,520e-3,200e-3,120e-3,80e-3,80e-3,360e-3,1.03,1.72,2.16,2.96,2.88])

T = 20 * np.log10(V_out / V_in)

fig, ax1 = plt.subplots()

ax1.plot(w_notch, 20*np.log10(np.abs(h_notch)), label='Teórica', linewidth=2)
ax1.plot(f, T, 'o', label='Mediciones', markersize=6, color='#f51414', markeredgecolor='white', markeredgewidth=1)
ax1.set_xlabel('Frecuencia[HZ]', fontsize=12)
ax1.set_ylabel('Magnitud[DB]', fontsize=12)
ax1.set_title('Filtro B: Notch IIR', fontsize=14, fontweight='bold')
ax1.legend(fontsize=11, loc='best')
ax1.grid(True, which='both',color='black', alpha=0.3)
ax1.tick_params(labelsize=10)

ax1.set_xlim([30, 70])

ax1.set_ylim([-50, 5])

plt.tight_layout()
plt.show()

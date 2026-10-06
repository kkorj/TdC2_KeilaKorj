#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:10:52 2026

@author: keila
"""
import numpy as np
from IPython.display import display, Math

f0=6e3
Q_plantilla=3

alfa_max=2.5#db
alfa_min=15#dB

fs1=600
fs2=60e3

ws1=fs1/f0
ws2=fs2/f0

alfa_max=2.5#db

epsilon2=10**(2.5/10)-1

epsilon=np.sqrt(epsilon2)

Q_sos=epsilon*Q_plantilla

#IMPLEMENTACIÓN MFB

import sympy as sp

S,G1,G2,G3,C1,C2=sp.symbols('S G1 G2 G3 C1 C2')
VA,Vi,Vo=sp.symbols('VA Vi Vo')

eqs=[
    VA*(S*(C1+C2)+G1+G2)-Vo*S*C1-Vi*G1,
    G3*Vo+S*C2*VA
]

sol=sp.solve(eqs,[VA,Vo])

T1 = sp.simplify(sol[Vo]/Vi)


num, den = sp.fraction(T1)
a = sp.Poly(den, S).coeff_monomial(S**2)
num_m = sp.simplify(num / a)
den_m = sp.expand(den / a)
display(Math(rf"T(s)=\frac{{{sp.latex(num_m)}}}{{{sp.latex(den_m)}}}"))

#VALORES DE LA IMPLEMENTACIÓN

k=-Q_sos**2
c=100e-9 #valor de capacidad objetivo
omega_w=6e3*2*np.pi #frecuencia 

omega_z=1/(c*omega_w)

#Valores de componentes normalizados
R1=-Q_sos/k
R2=Q_sos/(2*Q_sos**2+k)
R3=2*Q_sos

#Desnormalizados
R1=R1*omega_z
R2=R2*omega_z
R3=R3*omega_z

display(Math(rf"k={k:.4f}"))
display(Math(rf"R_1={R1:.4f}"))
display(Math(rf"R_2={R2:.4f}"))
display(Math(rf"R_3={R3:.4f}"))
display(Math(rf"C_1={c}"))
display(Math(rf"C_2={c}"))

#VALORES REALES

w0=6e3*2*np.pi
C1=97e-9
C2=103e-9

R3=(Q_sos/w0)*((C1+C2)/(C1*C2))
R1=-(R3/k)*(C2/(C1+C2))
R2=R1/(w0**2*C1*C2*R3*R1-1)

display(Math(rf"R_1={R1:.4f}"))
display(Math(rf"R_2={R2:.4f}"))
display(Math(rf"R_3={R3:.4f}"))


#MEDICIONES OSCILOCOPIO
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sig

plt.style.use('seaborn-v0_8-darkgrid')

w0 = 6e3 * 2 * np.pi
Q_sos = 2.3328
k = -Q_sos**2

# Transferencia teorica de referencia
num = [k * w0 / Q_sos, 0]
den = [1, w0 / Q_sos, w0**2]
T_esperada = sig.TransferFunction(num, den)

w = np.logspace(np.log10(500 * 2 * np.pi), np.log10(60e3 * 2 * np.pi), 10000)
w, mag, phase = sig.bode(T_esperada, w)

# Mediciones tomadas en el laboratorio
f = np.array([600, 2800, 3900, 5000, 5250, 5500, 5750, 6000, 6250, 6500, 6750, 7000, 21e3, 35e3, 50e3, 60e3])
V_in = np.array([1.58, 1.63, 1.15, 1.62, 1.53, 1.44, 1.34, 1.25, 1.17, 1.13, 1.12, 1.10, 1.24, 1.25, 1.26, 1.26])
V_out = np.array([0.416, 1.85, 2.75, 6.78, 7.11, 7.23, 7.15, 6.88, 6.48, 6.05, 5.65, 5.3, 1.03, 0.61, 0.43, 0.362])
dt = np.array([440, 108, 84, 78, 80, 80, 82, 82, 82, 84, 84, 84, 34.8, 21, 15, 12.4]) * 1e-6

T_medida = 20 * np.log10(V_out / V_in)
fase_medida = f * dt * -360

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Grafico de Magnitud
ax1.plot(w / (2 * np.pi), mag, label='Teórica', linewidth=2)
ax1.plot(f, T_medida, 'o', label='Mediciones', markersize=6, color='#f51414', markeredgecolor='white', markeredgewidth=1)
ax1.set_ylabel('Magnitud [dB]', fontsize=12)
ax1.set_title('Diagrama de Bode - Filtro Pasabanda Chebyshev', fontsize=14, fontweight='bold')
ax1.legend(fontsize=11, loc='best')
ax1.grid(True, which='both', color='black', alpha=0.3)
ax1.set_xscale('log')

# Grafico de Fase
ax2.plot(w / (2 * np.pi), phase, label='Teórica', linewidth=2, color='#2E86AB')
ax2.plot(f, fase_medida, 'o', label='Mediciones', markersize=6, color='#f51414', markeredgecolor='white', markeredgewidth=1)
ax2.set_xlabel('Frecuencia [Hz]', fontsize=12)
ax2.set_ylabel('Fase [°]', fontsize=12)
ax2.legend(fontsize=11, loc='best')
ax2.grid(True, which='both', color='black', alpha=0.3)
ax2.set_xscale('log')

plt.tight_layout()
plt.show()


#MEDICIONES ANALIZADOR DE AUDIO

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')

def leer_sweep(filename):
    with open(filename) as f:
        lines = f.readlines()
    f1_start = 3
    f1_end = next(i for i in range(f1_start, len(lines)) if lines[i].strip() == '')
    f1 = pd.read_csv(filename, skiprows=3, nrows=f1_end - f1_start - 1, names=['f_in', 'f_out'])
    f2_start = f1_end + 4
    f2 = pd.read_csv(filename, skiprows=f2_start, names=['f', 'dBr'])
    return f1, f2

_, sweep3 = leer_sweep('Sweep Data_3.csv')
_, sweep4 = leer_sweep('Sweep Data_4.csv')

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(sweep3['f'], sweep3['dBr'], label='Sweep 1 (5 Hz - 80 kHz)', linewidth=2, color='#2E86AB')
ax.plot(sweep4['f'], sweep4['dBr'], label='Sweep 2 (3 kHz - 10 kHz)', linewidth=2, color='#A23B72')
ax.set_xscale('log')
ax.set_xlabel('Frecuencia [Hz]', fontsize=12)
ax.set_ylabel('Magnitud [dBr]', fontsize=12)
ax.set_title('Magnitud Medida con Analizador de Audio', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.grid(True, which='both', color='black', alpha=0.3)
plt.tight_layout()
plt.show()
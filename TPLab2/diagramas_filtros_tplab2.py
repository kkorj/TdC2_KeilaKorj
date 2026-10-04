#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 00:59:32 2026

@author: keila
"""

import matplotlib.pyplot as plt
from scipy import signal as sig

plt.style.use('seaborn-v0_8-darkgrid')


##########################FILTRO NOTCH IIR########################
f = np.array([40,45,49,49.2,49.5,49.7,49.9,50,50.2,50.5,50.7,50.9,51,55,60])
V_in = np.array([3.35,3.27,3.27,3.16,3.35,3.24,3.24,3.16,3.11,3.11,3.11,3.03,3.11,3.27,3.31])
V_out = np.array([3.03,2.96,2.24,1.55,520e-3,200e-3,120e-3,80e-3,80e-3,360e-3,1.03,1.72,2.16,2.96,2.88])

T = 20 * np.log10(V_out / V_in)

fig, ax1 = plt.subplots()

ax1.plot(w, 20*np.log10(np.abs(h)), label='Teórica', linewidth=2)
ax1.plot(f, T, 'o', label='Mediciones', markersize=6, color='#f51414', markeredgecolor='white', markeredgewidth=1)
ax1.set_xlabel('Frecuencia[HZ]', fontsize=12)
ax1.set_ylabel('Magnitud[DB]', fontsize=12)
ax1.set_title('Filtro Notch IIR', fontsize=14, fontweight='bold')
ax1.legend(fontsize=11, loc='best')
ax1.grid(True, which='both',color='black', alpha=0.3)
ax1.tick_params(labelsize=10)

ax1.set_xlim([30, 70])

ax1.set_ylim([-50, 5])

plt.tight_layout()
plt.show()

##########################FILTRO PASABAJOS FIR##############################
f = np.array([30,50,70,80,90,100,110,130,150,200,300])
V_in = np.array([2.11,2.20,2.15,2.16,2.16,2.11,2.1,2.07,2.07,2.05,2.05])
V_out = np.array([1.96,1.87,1.75,1.67,1.63,1.60,1.51,1.27,1.08,0.576,0.02])

T = 20 * np.log10(V_out / V_in)

fig, ax1 = plt.subplots()

ax1.plot(wfir,magfir, label='Teórica', linewidth=2)
ax1.plot(f, T, 'o', label='Mediciones', markersize=6, color='#f51414', markeredgecolor='white', markeredgewidth=1)
ax1.set_xlabel('Frecuencia[HZ]', fontsize=12)
ax1.set_ylabel('Magnitud[DB]', fontsize=12)
ax1.set_title('Filtro Pasabajos FIR', fontsize=14, fontweight='bold')
ax1.legend(fontsize=11, loc='best')
ax1.grid(True, which='both',color='black', alpha=0.3)
ax1.tick_params(labelsize=10)

ax1.set_xlim([0, 500])

ax1.set_ylim([-50, 5])

plt.tight_layout()
plt.show()
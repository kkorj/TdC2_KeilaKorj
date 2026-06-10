#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:50:41 2026

@author: keila
"""
# Inicialización e importación de módulos

# Módulos externos
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig

fig_sz_x = 13
fig_sz_y = 7
fig_dpi = 80 # dpi

fig_font_size = 11

mpl.rcParams['figure.figsize'] = (fig_sz_x, fig_sz_y)
mpl.rcParams['figure.dpi'] = fig_dpi
plt.rcParams.update({'font.size':fig_font_size})

from pytc2.sistemas_lineales import analyze_sys, pretty_print_bicuad_omegayq, tf2sos_analog, pretty_print_SOS, pretty_print_lti

from pytc2.general import print_subtitle

alpha_max = 0.5 #Ripple de la plantilla en dB

alpha_min= 30 #atenuación de la plantila en dB

eps_2= 10**(alpha_max/10) - 1 #Espsilon cuadrado

w_s=4

#BONUS 1: MAXIMA PLANICIDAD CHEQUEO DE PLANTILLA SI ES POSIBLE

for nn in np.arange(start = 1, stop= 6):
    
    alpha_n = 10* np.log10(1+ (eps_2*w_s**(2*nn)))
    
    print(f'Para n ={nn} es alpha_n es de {alpha_n: 3.3f} dB')
    
    if alpha_n >= alpha_min:
        orden=nn
        break



print(f'Para cumplir con la plantila en Máxima Planicidad se necesita un orden {orden} ya que se obtuvo un alpha_n de {alpha_n: 3.3f} dB que es mayo o a alpha_min={alpha_min} dB')


#Bonus 2 chequeo cheby

print('CHEBYYYYY')

for nn in np.arange(start = 1, stop= 6):
    
   dentro_cosh = nn * np.arccosh(w_s)
   alpha_n = 10 * np.log10(1 + eps_2 * (np.cosh(dentro_cosh)**2))
    
   print(f'Para n ={nn} es alpha_n es de {alpha_n: 3.3f} dB')
    
   if alpha_n >= alpha_min:
        orden=nn
        break



print(f'Para cumplir con la plantila en Chebychev se necesita un orden {orden} ya que se obtuvo un alpha_n de {alpha_n: 3.3f} dB que es mayo o a alpha_min={alpha_min} dB')


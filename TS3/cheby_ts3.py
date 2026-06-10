#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:25:06 2026

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


this_order = 3

this_ripple = 0.5

z,p,k = sig.cheb1ap(this_order, this_ripple)

num, den = sig.zpk2tf(z,p,k)

lp_cheby = tf2sos_analog(num, den)

print("LP Cheby")

pretty_print_lti(num, den)

#IMPRIMO GRAFS DE CHEBY LP

#analyze_sys(lp_cheby, 'LP Cheby')

#PASAMOS A UN CHEBY HP

num_hp, den_hp = sig.lp2hp(num, den)

hp_cheby = tf2sos_analog(num_hp, den_hp)

print("HP Cheby")

pretty_print_lti(num_hp, den_hp)

print("HP Cheby dividida en secciones")

pretty_print_SOS(hp_cheby)
#Ahora HP desnormalizado en frec:
    
num_hp_des, den_hp_des = sig.lp2hp(num, den, 2 * np.pi * 40e3)


print("HP Cheby desnomralizado")

pretty_print_lti(num_hp_des, den_hp_des)

##IMPRIME GRAFICOS DE HP CHEBY

analyze_sys(hp_cheby, 'HP Cheby')


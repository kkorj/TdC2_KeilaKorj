#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 16:39:26 2026

@author: keila
"""

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



z,p,k = sig.besselap(this_order, norm='delay')

num, den = sig.zpk2tf(z,p,k)

lp_bessel = tf2sos_analog(num, den)

print("LP Bessel Orden 3")

pretty_print_lti(num, den)

print("LP Bessel Orden 3 dividida en secciones")

pretty_print_SOS(lp_bessel)

#Ahora LP desnormalizado en frec:
#   
#num_lp_des, den_lp_des = sig.lp2lp(num, den, )


#print("LP Bessel desnomralizado")

#pretty_print_lti(num_lp_des, den_lp_des)


#IMPRIMO GRAFS DE BESSEL LP

#analyze_sys(lp_bessel, 'LP Bessel')


#BONUS 1

#ORDEN 2
this_order = 2


z,p,k = sig.besselap(this_order, norm='delay')

num, den = sig.zpk2tf(z,p,k)

lp_bessel = tf2sos_analog(num, den)

print("LP Bessel Orden 2")

pretty_print_lti(num, den)

#ORDEN 4
this_order = 4


z,p,k = sig.besselap(this_order, norm='delay')

num, den = sig.zpk2tf(z,p,k)

lp_bessel = tf2sos_analog(num, den)

print("LP Bessel Orden 4")

pretty_print_lti(num, den)
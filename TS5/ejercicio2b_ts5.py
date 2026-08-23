# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
#import matplotlib as mpl
from matplotlib import pyplot as plt

# módulo de SciPy
from scipy import signal as sig

from pytc2.sistemas_lineales import analyze_sys, bodePlot, pzmap, pretty_print_bicuad_omegayq

#Normalizo el valor de los componentes
C = 1 
L = 1

#TRANSFERENCIA V23/V13:

num = np.array([ 1/(C*L) ])
den = np.array([ 1, 0, 1/(C*L) ])

H1 = sig.TransferFunction( num, den )

# Otra forma de analizar el sistema H1, con una función
# de más alto nivel. Podés probarlo si te interesa.

# el caracter "_" descarta la salida de la función
bodePlot(H1, 'TRANSFERENCIA V23/V13')

#TRANSFERENCIA V21/V31 y V12/V32:


num = np.array([ 1, 0, 0 ])
den = np.array([ 1, 0, 1/(C*L) ])

H1 = sig.TransferFunction( num, den )

# Otra forma de analizar el sistema H1, con una función
# de más alto nivel. Podés probarlo si te interesa.

# el caracter "_" descarta la salida de la función

bodePlot(H1, 'TRANSFERENCIA V21/V31 y V12/V32')


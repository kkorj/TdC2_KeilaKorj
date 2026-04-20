# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
#import matplotlib as mpl
#from matplotlib import pyplot as plt

# módulo de SciPy
from scipy import signal as sig

from pytc2.sistemas_lineales import analyze_sys, bodePlot, pzmap, pretty_print_bicuad_omegayq


# Cargamos la funcion transferencia como vectores de sus coeficientes.

num = np.array([ 1, -1 ])
den = np.array([ 1., 1 ])

H1 = sig.TransferFunction( num, den )

# Otra forma de analizar el sistema H1, con una función
# de más alto nivel. Podés probarlo si te interesa.

# el caracter "_" descarta la salida de la función
_ = analyze_sys([H1], sys_name='pasa todo')



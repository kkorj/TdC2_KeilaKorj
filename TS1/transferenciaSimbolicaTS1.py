#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:16:20 2026

@author: keila
"""

import sympy as sp
from pytc2.remociones import remover_polo_dc
from pytc2.general import a_equal_b_latex_s, print_latex, s, symbfunc2tf, factorSOS
from pytc2.sistemas_lineales import bodePlot

from IPython.display import display, Math

# tensiones y corrientes que usaremos para nuestros análisis
V1, V2, Va = sp.symbols("V1, V2, Va")
Y1, Y2, Y3, Yc = sp.symbols("Y1, Y2, Y3, Yc")
R1, R2, R3, C1 = sp.symbols("R1, R2, R3, C1")



aa = sp.solve([ 
                Va*(Y3 + Yc) - V1*Yc, Va*(Y1 + Y2) - V1*Y1 - V2*Y2
                ], 
                [V1, V2, Va])
T_s = aa[V2]/aa[V1]

T_s1=sp.simplify(sp.expand(T_s.subs({Y1:1/R1, Y2:1/R2, Y3:1/R3, Yc:s*C1})))

print_latex(a_equal_b_latex_s('T(s)= \\frac{V_2}{V_1}', T_s1))


#Chequeo con normalización

O_z, O_w0, s, s_n = sp.symbols("O_z, O_w0, s, s_")

aa = sp.solve([ 
                Va*(Y3 + Yc) - V1*Yc, Va*(Y1 + Y2) - V1*Y1 - V2*Y2
                ], 
                [V1, V2, Va])
T_s = aa[V2]/aa[V1]

T_s1=sp.simplify(sp.expand(T_s.subs({O_z:R3, O_w0: 1/(R3*C1), s: (s_n)*O_w0, Y1:1/(R1/O_z), Y2:1/(R2/O_z), Y3:1/(R3/O_z), Yc:s*(C1*O_z)})))

# En Yc:s*(C1*O_z) solo pongo el O_z porque al ya reemplazar s por s: (s_n)*O_w0 ahí ya incluyo a O_w0

print_latex(a_equal_b_latex_s('T(s)= \\frac{V_2}{V_1}', T_s1))

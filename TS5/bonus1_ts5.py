#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 21:37:50 2026

@author: keila
"""

import sympy as sp

from pytc2.cuadripolos import calc_MAI_impedance_ij, calc_MAI_vtransf_ij_mn, calc_MAI_ztransf_ij_mn
from pytc2.general import print_latex


s, Y_C, Y_L = sp.symbols('s Y_C Y_L', complex=True)

C, L = sp.symbols('C L', complex=True)



# Armo la MAI

#               Nodos:                     0                                1                                              2        
Ymai = sp.Matrix([  
                    [ ((Y_L**2) + (Y_L*Y_C))/((2*Y_L)+Y_C),   -(Y_L**2)/((2*Y_L)+Y_C),                      -(Y_L*Y_C)/((2*Y_L)+Y_C)],
                    [      -(Y_L**2)/((2*Y_L)+Y_C),          ((Y_L**2) + (Y_L*Y_C))/((2*Y_L)+Y_C),          -(Y_L*Y_C)/((2*Y_L)+Y_C)],
                    [      -(Y_L*Y_C)/((2*Y_L)+Y_C),          -(Y_L*Y_C)/((2*Y_L)+Y_C),                     2*(Y_L*Y_C)/((2*Y_L)+Y_C)]
                 ])


#Asigno componentes a Y_L e Y_C

Ymai = Ymai.subs(Y_L, 1/(s*L))
Ymai = Ymai.subs(Y_C, (s*C))


#Obtengo las transferencias del ejercicio 2a:
    
#TRANSFERENCIA V23/V13:
    
Vmai = calc_MAI_vtransf_ij_mn(Ymai, 1, 2, 0, 2)

print('TRANSFERENCIA V23/V13:')
print_latex( r'T^{{ {:d}{:d} }}_{{ {:d}{:d} }} = '.format(2,3,1,3) +  sp.latex(Vmai) )


#TRANSFERENCIA V21/V31:
    
Vmai = calc_MAI_vtransf_ij_mn(Ymai, 1, 0, 2, 0)

print('TRANSFERENCIA V21/V31:')
print_latex( r'T^{{ {:d}{:d} }}_{{ {:d}{:d} }} = '.format(2,1,3,1) +  sp.latex(Vmai) )


#TRANSFERENCIA V12/V32:
    
Vmai = calc_MAI_vtransf_ij_mn(Ymai, 0, 1, 2, 1)

print('TRANSFERENCIA V12/V32:')
print_latex( r'T^{{ {:d}{:d} }}_{{ {:d}{:d} }} = '.format(1,2,3,2) +  sp.latex(Vmai) )

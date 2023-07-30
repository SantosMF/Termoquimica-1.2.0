#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:49:49 2021

@author: marcio
"""
import modulo1 as modulo
import readline
import sys
readline.parse_and_bind('tab: complete')
scfout = str(input('Insira o arquivo scf.out:\n>> '))
dynout = str(input('Insira o arquivo dyn.out:\n>> '))
temp =  str(input('Insira as temperaturas mínima, máxima e deltaT, separadas por vírgula:\n>> '))
sistema = str(input('Sólidos ou Moléculas/Átomos? (s ou m):\n>> '))
Tmin = temp.split(',')[0]
Tmax = temp.split(',')[1]
dT = temp.split(',')[2]
def Save(i):
    print(107*'=')
    print(i)
    print(107*'=')
    salvar = str(input('Deseja salvar os dados? (s/N)\n>> '))
    if salvar == 's':
        with open(str(input('Nome para o arquivo\n>> ')),'w') as out:
            out.write(i)
    else: sys.exit()
if sistema == 's':
    valores = ['solido', scfout, dynout, Tmin, Tmax, 0, 0, 0, dT]
    resultado = modulo.Termo(valores)
    Save(resultado)
elif sistema == 'm':
    tipo = str(input('Linear, não-linear ou monoatômico? (l, nl, ma):\n>> '))
    if tipo == 'l':
        S = int(input('Número de simetria? \n>> '))
        P = float(input('Pressão? (em atm):\n>> '))
        valores = ['molecula', scfout, dynout, Tmin, Tmax, P, S,'linear' , dT]
        resultado = modulo.Termo(valores)
        Save(resultado)
    if tipo == 'nl':
        S = int(input('Número de simetria? \n>> '))
        P = float(input('Pressão? (em atm):\n>> '))
        valores = ['molecula', scfout, dynout, Tmin, Tmax, P, S,'nolinear' , dT]
        resultado = modulo.Termo(valores)
        Save(resultado)
    elif tipo == 'ma':
        P = float(input('Pressão? (em atm):\n>> '))
        valores = ['molecula', scfout, dynout, Tmin, Tmax, P, S, 'atomo', dT]
        resultado = modulo.Termo(valores)
        Save(resultado)

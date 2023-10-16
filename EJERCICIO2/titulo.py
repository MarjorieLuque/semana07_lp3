# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:35:09 2023

@author: Alumno
"""
# Importamos la libreria

nombre = "marjorie nikhol luque cardenas"

import camelcase
print(nombre.upper())
print(nombre.title())

#Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase....")

# imprimimos el nombre en formato título
# utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# creamos otro objeto llamado cam2
# al definir el objeto, incluimos los argumentos
# 'marjorie' y 'luque' 
cam2 = camelcase.CamelCase('marjorie','luque')
print(cam2.hump(nombre))

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:09:13 2023

@author: Alumno
"""

archivo = open("archivo_de_prueba.txt", "wt")
contenido = "Línea1 hola amigos como están?\nLínea2 Bienvenido a UNTELS"
archivo.write(contenido)
archivo.close()


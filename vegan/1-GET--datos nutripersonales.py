#! /usr/bin/env python
# -*- coding: utf-8 -*-

#####
#This file is part of VeganCookie.
#
#    VeganCookie is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Foobar is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#####


print "Programa vegano, para conocer el gasto calorico por dia\n"

print "Edad"
edad=float(raw_input())
print "Peso"
peso=float(raw_input())
print "talla en cm"
talla=float(raw_input())

# C.A. ****falta

	
# Sexo
print "Sexxxo[hombre-mujer]"
sexo=raw_input()
if sexo=="hombre":
	TMB=66+(13.7*peso)+(5*talla)-(6.8*edad)
	print "Coeficiente de Actividad(alto-medio-bajo--o especifica):"
	cantidad=raw_input()
	if cantidad=="alto":
		CA=2.10
	elif cantidad=="medio":
		CA=1.78
	elif cantidad=="bajo":
		CA=1.55
	else:
		CA=float(cantidad)
elif sexo=="mujer":
	TMB=655+(9.7*peso)+(1.8*talla)-(4.7*edad)	
	print "Coeficiente de Actividad en la Mujer(alto-medio-bajo--numero):"
	cantidad=raw_input()
	if cantidad=="alto":
		CA=1.82
	elif cantidad=="medio":
		CA=1.64
	elif cantidad=="bajo":
		CA=1.56
	else:
		CA=float(cantidad)
else:
	print "prueba con 'hombre' o 'mujer'"
# Proteinas
print "Consumo de proteinas(normal-alta)"

proteina=raw_input()

if proteina=="normal":
	ETA=TMB*0.1
elif proteina=="alta":
	ETA=TMB*0.15


GET= TMB*CA + ETA
IMC= peso/((talla/100)**2)

print "GET", GET,"IMC",IMC





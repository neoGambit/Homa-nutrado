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

# Da tu gasto energetico total en Kcal y obten una recomendacion en equivalentes:
print "Programa Vegano, para obtener el numero de equivalentes(smae) por grupos alimenticios, en base al gasto calorico particular.\n"

getfinal=[]
getNuevo=[]
equivalentes=0

#GRUPOS ALIMENTICIOS
#
#Vegana		=["Verduras","Frutas","Cereales","Leguminosas","Semillas","Grasas","Azucar"]
#ovovegetariana	=["Verduras","Frutas","Cereales","Leguminosas","Semillas","Grasas","Azucar"]
#Ovolactovegan  =["Verduras","Frutas","Cereales","Leguminosas","Semillas","Grasas","Azucar",LACTEOS]
#Omnivora	=["Verduras","Frutas","Cereales","Leguminosas","Semillas","Grasas","Azucar","LACTEOS","AOA"]

#Aclaraciones
#
#Cereales	="Cereales y tuberculos"
#SEMILLAS	="Grasas con proteinas"

GET=float(raw_input("Tu GET es:"))
print "Dieta vegana recomendada:"

#MOD-equivalentes basicos +2 en frutas -1 en semillas=AOA
get1200=[3,5,5,1.0,3,3,1]
get1400=[5,5,5,1.0,3,3,1]
get1600=[6,6,6,1.0,4,3,1]
get1800=[6,6,7,1.0,6,4,2]
get2000=[6,6,8,1.5,6,4,3]
get2200=[7,7,8,2.0,6,5,3]
getTodos=[get1200,get1400,get1600,get1800,get2000,get2200]
#Vegana=["Verduras","Frutas","Cereales","Leguminosas","Semillas","Grasas","Azucar"]
#MOD-Vegano

###################################GETs basicos
if 1150<=GET<2250:
	i=0
	while i<6:
		if ((1200+i*200)-50)<=GET<((1200+i*200)+50):
			getfinal=getTodos[i]
			i=i+6
		else:
			i=i+1
####################################GETs compuestos

elif 2350<=GET<4450:
	i=0
	j=0	#para el get q se suma
	k=0 #para el get q se suma
	while i<11:   #for i in range(11):
		if (2400+i*200)-50<=GET<(2400+i*200)+50:
			for l in range(len(get1200)):
				equivalentes=getTodos[j][l]+getTodos[k][l] 
				getNuevo.append(equivalentes)
			#evita tanta vuelta:
			i=i+11
		elif j<=4:
			j=j+1
		elif k<5:
			k=k+1
		i=i+1	
	getfinal=getNuevo
	print getfinal	

####################  MultiCompuestos

## 4600
elif 4550<=GET<4650:
	for i in range(len(get1200)):
		equivalentes=get1600[i]+get1600[i]+get1400[i]
		getNuevo.append(equivalentes)
	getfinal=getNuevo
	print getfinal

## 4800
elif 4750<=GET<=4850:
	for i in range(len(get1200)):
		equivalentes=get1600[i]+get1600[i]+get1600[i]
		getNuevo.append(equivalentes)
	getfinal=getNuevo
	print getfinal
elif 4850<GET:
	print "Felicidades!, eres un bizonte muy activo!"
	#aqui debe ir una función de cierre del programa
else:
	print "Tu GET no esta contemplado, suma o resta 50 Kcal y vuelve a intentar"

print "Dieta Recomendada:"

#grupos=['VERDURAS','FRUTAS','CEREALES Y TUBERCULOS','LEGUMINOSAS','AOA','LACTEOS','GRASAS','AZUCAR']
grupos=	['VERDURAS','FRUTAS','CEREALES','LEGUMINOSAS','SEMILLAS','GRASAS','AZUCAR']

i=0
for i in range(len(grupos)):
	print getfinal[i],"equivalentes de",grupos[i]
'''
#MOD-equivalentes basicos
get1200=[3,3,5,1.0,4,3,1]
get1400=[5,3,5,1.0,4,3,1]
get1600=[6,4,6,1.0,5,3,1]
get1800=[6,4,7,1.0,7,4,2]
get2000=[6,4,8,1.5,7,4,3]
get2200=[7,5,8,2.0,7,5,3]
getTodos=[get1200,get1400,get1600,get1800,get2000,get2200]
#Vegana=["Verduras","Frutas","Cereales","Leguminosas","Semillas","Grasas","Azucar"]
#MOD-Vegano
'''

'''
#MOD-equivalentes basicos
get1200=[3,3,5,1.0,4,3,1,4,1]
get1400=[5,3,5,1.0,4,3,1,4,2]
get1600=[6,4,6,1.0,5,3,1,5,2]
get1800=[6,4,7,1.0,7,4,2,6,2]
get2000=[6,4,8,1.5,7,4,3,7,2]
get2200=[7,5,8,2.0,7,5,3,7,2]
getTodos=[get1200,get1400,get1600,get1800,get2000,get2200]
#Vegana=["Verduras","Frutas","Cereales","Leguminosas","Semillas","Grasas","Azucar","AOA","LACTEOS"]
#MOD-Omnivora ya ordenada
'''
'''
#MOD-equivalentes basicos
get1200=[3,3,5,1.0,4,1,3,1]
get1400=[5,3,5,1.0,4,2,3,1]
get1600=[6,4,6,1.0,5,2,3,1]
get1800=[6,4,7,1.0,6,2,4,2]
get2000=[6,4,8,1.5,7,2,4,3]
get2200=[7,5,8,2.0,7,2,5,3]
getTodos=[get1200,get1400,get1600,get1800,get2000,get2200]
#grupos=['VERDURAS','FRUTAS','CEREALES Y TUBERCULOS','LEGUMINOSAS','AOA','LACTEOS','GRASAS','AZUCAR']
#MOD-Omnivora
'''

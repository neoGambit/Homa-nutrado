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

print "Programa Vegano, para refinar el numero de equivalentes de acuerdo a las proporciones de grasa, proteina, y carbohidratos sugerida.\n"

# Tu proporcionas tus equivalentes propuestos y te muestra el aporte energetico total. Tambien la cantidad en gramos de grasa, proteinas y carbohidratos(490 gr de carbohidratos,)

#Para un dieta de 2800 kcal, con porcentajes de 70%Ch,20%Li,10%Pr
#proporcion_gramos=[490,grCh,62.2,grLi,70,grPr]

#Verduras(25kcal)->Frutas(60kcal)->Cereales y Tuberculos(70kcal)->leguminosas(120kcal)->Semillas(70kcal)->Grasas(45kcal)->Azucar(40kcal)
GET=float(raw_input("Tu GET es:")) #Para calcular gramos de Ch, li, y pr, segun 70%, 20%,10%]

#MOD-calorias (consultar pág. 12 de SMAE 3ra Ed.)
Grupo=		["Verduras","Frutas","Cereales","Leguminosas","Semillas","Grasas","Azucar"]
#		[ Ve,	Fr,	Ce,	Le,	Se,	Gr,	Az]   
Calorias=	[24,	60,	68,	121,	69,	45,	40]
Carbohidratos=	[4,	15,	15,	20,	3,	0,	10]
Lipidos=	[0,	0,	0,	1,	5,	5,	0]
Proteinas=	[2,	1,	2,	8,	3,	0,	0]
#MOD-vegano

Totalkcal=0
Totalch=0
Totalli=0
Totalpr=0
### Calculos
for i in range(7):	#MOD-tutoj# [7 para vegano, 9 omnivoro(por AOA y lacteos ) ]
	Equivalentes = float(raw_input("Equivalentes de "+Grupo[i]+":\n"))
	Kcal= Equivalentes*Calorias[i]
	Totalkcal += Kcal
	Hc  = Equivalentes*Carbohidratos[i]
	Totalch += Hc
	Li  = Equivalentes*Lipidos[i]
	Totalli += Li
	Pr  = Equivalentes*Proteinas[i]
	Totalpr += Pr
### GET y gramos recomendados segun 70%, 20%,10%
recomendado_Ch=	int(	(GET*.70)/4)
recomendado_Li=	int(	(GET*.20)/9)
recomendado_Pr=	int(	(GET*.10)/4)
### Segun los eqs propuestos, los porcentajes alcanzados
pc_Ch= int(	(Totalch)*(400)/Totalkcal)       # gr=(total*0.7)/4 despejando el %
pc_Li= int(	(Totalli)*(900)/Totalkcal)
pc_Pr= int(	(Totalpr)*(400)/Totalkcal)
#### Resultados
print "Kcal:",Totalkcal
print "Carbohidratos(",recomendado_Ch,"recom.)",Totalch,"(Es el ",pc_Ch,"% de ",Totalkcal,")"
print "Lipidos(",recomendado_Li,"recom.)",Totalli,"(Es el ",pc_Li,"% de ",Totalkcal,")"
print "Proteina(",recomendado_Pr,"recom.)",Totalpr,"(Es el ",pc_Pr,"% de ",Totalkcal,")"
####

print "fin"

#
'''
#MOD-calorias (consultar pág. 12 de SMAE 3ra Ed.)
Grupo=		["Verduras","Frutas","Cereales","Leguminosas","Semillas","Grasas","Azucar"]
#		[ Ve,	Fr,	Ce,	Li,	Se,	Gr,	Az]   
Calorias=	[24,	60,	68,	121,	69,	45,	40]
Carbohidratos=	[4,	15,	15,	20,	3,	0,	10]
Lipidos=	[0,	0,	0,	1,	5,	5,	0]
Proteinas=	[2,	0,	2,	8,	3,	0,	0]
#MOD-vegano
'''
#


#
'''
#MOD-calorias
Grupo=		["Verduras","Frutas","Cereales","Leguminosas","Semillas","Grasas","Azucar","Lacteos","Huevos"]
#		[ Ve,	Fr,	Ce,	Li,	Se,	Gr,	Az,	La,	Hu]   
Calorias=	[24,	60,	68,	121,	69,	45,	40,	156,	75,]
Carbohidratos=	[4,	15,	15,	20,	3,	0,	10,	12,	0,]
Lipidos=	[0,	0,	0,	1,	5,	5,	0,	8,	5,]
Proteinas=	[2,	0,	2,	8,	3,	0,	0,	9,	7,]
#MOD-Ovolactovegetariano
'''
#

'''Grupos en el Sistema Mexicano de Alimentos Equivalentes(SMAE)
Verduras
Frutas
Cereales sin grasa
Cereales con grasa
Leguminosas
#AOA
leche descremada
leche semidescremada
leche entera
leche con azúcar
aceites y grasas
aceites y grasas con proteína
azucares sin grasa
bebidas alcohólicas
libre
#Productos comerciales
'''

'''Grupos de MOD-vegan
Verduras
Frutas
Cereales
Leguminosas
Semillas
Grasas
Azucar
'''

'''Grupos de MOD-Ovolactovegetariano
vegan+
Lacteos(entera)
huevos cocidos
'''





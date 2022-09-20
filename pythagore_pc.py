###########################################
#                                         #
#             |¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|          #
#             |    |¯¯¯¯¯¯¯|   |          #  
#             |    |       |   |          #
#             |    |       |   |          #
#             |    |_______|   |          #
#             |    ____________|          #
#             |    |                      #
#             |    |                      #
#             |    |                      #
#             |    |                      #
#             |    |                      #
#             |____|         By Picsald   #
###########################################

from tkinter import messagebox

#TOUJOURS METTRE LE NOM DE L'ANGLE DROIT EN DEUXIEME
nom_triangle=input("ⓘ Quelle est le nom du triangle ?")

#Convertion du nom du triangle en liste
nom_triangle_list=list(nom_triangle.strip())

#Nom des longueur
nom_longueur_1=nom_triangle_list[0]+nom_triangle_list[1]
nom_longueur_2=nom_triangle_list[1]+nom_triangle_list[2]
nom_hypotenuse=nom_triangle_list[0]+nom_triangle_list[2]

#Les question posé pour savoir le nom du triangle et les longuueur

longueur_1=int(input("ⓘ Quelle est la longueur "+nom_longueur_1+ " ? "))
longueur_2=int(input("ⓘ Quelle est la longueur "+nom_longueur_2+ " ? "))
longueur_1_str=str(longueur_1)
longueur_2_str=str(longueur_2)

#calcule
carre_1=longueur_1**2
carre_1_str=str(carre_1)
carre_2=longueur_2**2
carre_2_str=str(carre_2)
addition_carre_1_2=carre_1 + carre_2
addition_carre_1_2_str=str(addition_carre_1_2)
hypotenuse=addition_carre_1_2 **0.5
hypotenuse_str=str(hypotenuse)

#affichage de la réponse a copier

print ("  Le triangle "+nom_triangle+" est rectangle en "+nom_triangle_list[1]+".")
print (" D'après le théoreme de Pythagore : ")
print ("     "+ nom_longueur_1 +"² + "+ nom_longueur_2 +"² = "+nom_hypotenuse+"²")
print ("     "+longueur_1_str+"² + "+longueur_2_str+"² = "+nom_hypotenuse+"²")
print ("     "+carre_1_str+" + "+carre_2_str+" = "+addition_carre_1_2_str)
print (" Donc "+nom_hypotenuse+" = "+addition_carre_1_2_str+" = √"+addition_carre_1_2_str+" = "+hypotenuse_str)
print ("Donc on en conclut que la longueur de l'hypotenuse "+nom_hypotenuse+" est : "+ hypotenuse_str)

#Fin
input("ⓘ Avez vous fini ?")


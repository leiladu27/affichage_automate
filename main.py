from lire_automate import *
from determinisation import *

automate=input("Quel automate voulez-vous tester ?")
a=lire_automate_sur_fichier(automate)
print(a)

a=determinisation_et_completion(a)
afficher_automate_deterministe_complet(a)
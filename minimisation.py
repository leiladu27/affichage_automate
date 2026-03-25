from determinisation import *
from lire_automate import *

def minimisation(AFDC) :
    fin = False
    k = 0 #compteur du nombre d'itérations pour trouver la partition finale
    theta = {"T": [], "NT": []}

    """
    Étape 1 : On crée une partition P0 = {"T": [], "NT": []}
    """
    #partition initiale
    for etat in AFDC["etats"] :
        if etat in AFDC["final"] :
            theta["T"].append(etat)
        else :
            theta["NT"].append(etat)

    print("Partition P0 :", theta)

    ancien_p = theta

    while not fin :
        k += 1
        motif = {}

        """
        Étape 2 : On crée les groupes d'état en séparant par motif avec leurs transitions
        """
        #on cherche le motif de chaque état
        print("Transitions :")
        for etat in AFDC["etats"] :
            motif[etat] = []
            for lettre in AFDC["alphabet"] :
                for t in AFDC["transitions"] :
                    if t[0] == etat and t[1] == lettre : #on vérifie que l'état et la lettre de la liste transitions correspondent à ceux dans le motif
                        for grp, etats in ancien_p.items() :
                            if t[2] in etats : #t[2] c'est les états d'arrivée
                                motif[etat].append(grp) #si on trouve l'état d'arrivée correspondant, on l'ajoute à notre groupe
            print(etat, ":", motif[etat])

        #on stocke séparément les états terminaux et les états non terminaux dans temp
        temp = [[], []]
        p = {} #dictionnaire des groupes d'état -> partition
        j = 1 #compteur pour la numérotation des groupes

        for e, m in motif.items() : #e est l'état et m son motif
            if e in AFDC["final"] :
                temp[0].append((e, m))
            else :
                temp[1].append((e, m))

        #on compare les motifs entre les états T pour faire les groupes
        for etat2, motif2 in temp[0] : #temp[0] contient les états terminaux
            trouve = False
            for grp2 in p :
                if motif[p[grp2][0]] == motif2 and p[grp2][0] in AFDC["final"] : #on compare uniquement les motifs des états T avec les autres états T
                    p[grp2].append(etat2)
                    trouve = True
                    break
            if not trouve :
                p["G" + str(j)] = [etat2]
                j += 1

        #on compare les motifs entre les états NT pour faire les groupes
        for etat3, motif3 in temp[1] : #temp[1] contient les états non terminaux
            trouve = False
            for grp3 in p:
                if motif[p[grp3][0]] == motif3 and p[grp3][0] not in AFDC["final"] : #on compare uniquement les motifs des états NT avec les autres états NT
                    p[grp3].append(etat3)
                    trouve = True
                    break
            if not trouve:
                p["G" + str(j)] = [etat3]
                j += 1

        print("")
        print("Partition P" + str(k), ":", p)

        """
        Étape 3 : On compare les partitions obtenues avec les anciennes partitions -> condition d'arrêt
        """
        if list(p.values()) == list(ancien_p.values()) : #si on obtient la même partition que celle d'avant, on s'arrête
            print("On obtient la même partition que P" + str(k-1) + ".")
            print("")
            print("Partition Finale :", p)
            fin = True
        ancien_p = p
    return p

AFDCM = minimisation(AFDC)

def afficher_automate_minimal(AFDCM) :
    tab_cp = {}
    i = 1

    #on crée la table de correspondance
    for etats in AFDCM.values() :
        tab_cp["G" + str(i)] = etats
        i += 1
    print("Table de correspondance :")

    for grp, etats in tab_cp.items():
        print(grp, "<-", etats)

    #on cherche l'état initial
    initial = []
    for grp, etats in tab_cp.items():
        if AFDC["initial"][0] in etats:
            initial = grp
            break

    #on cherche les états finaux
    final = []
    for grp, etats in tab_cp.items():
        for e in etats:
            if e in AFDC["final"]:
                final.append(grp)
                break

    #on calcule les transitions
    transitions = []
    for grp, etats in tab_cp.items():
        representant = etats[0] #on prend le premier état du groupe
        for lettre in AFDC["alphabet"]:
            for t in AFDC["transitions"]:
                if t[0] == representant and t[1] == lettre:
                    for grp2, etats2 in tab_cp.items(): #on cherche dans quel groupe se trouve t[2]
                        if t[2] in etats2:
                            transitions.append([grp, lettre, grp2])
                            break

    #on affiche sous le même format d'automates que nos fichiers txt
    print("etats:", end=" ")
    for grp in tab_cp.keys():
        print(grp, end=" ")
    print()

    print("alphabet:", end=" ")
    for lettre in AFDC["alphabet"]:
        print(lettre, end=" ")
    print()

    print("initial:", initial)

    print("final:", end=" ")
    for f in final:
        print(f, end=" ")
    print()

    print("transitions:")
    for t in transitions:
        print(t[0], t[1], t[2])


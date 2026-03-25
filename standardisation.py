def standardisation(AF):
    "Créer un nouvel état"
    "Parcourir la liste des transitions"
    "Si une transition mène à un état initial"
    "ajouter à la clé transition [nouvel état, libelé de la transition, état de départ de la transition]"
    "Supprimer la transition qui mène à l'état initial"
    "Ajouter le nouvel état après la fin du parcours"
    "Supprimer le ou les états de la clé initial(sauf le nouvel état)"
    nouvel_état = 'I'
    AF["etats"].insert(0, nouvel_état)
    for tr in AF['transitions']:
        if tr[0] == nouvel_état:
            continue
        elif tr[0] in AF['initial']:
            AF['transitions'].append([nouvel_état, tr[1], tr[2]])
    """for tr in AF['transitions']:
        for i in AF['initial']:
            if tr[0] == i and tr[0] != tr[2]:
                tr[0] = nouvel_état"""
    """if len(AF['initial'])>1:"""
    AF["initial"] = None
    AF["initial"] = [nouvel_état]
    #print(AF)
    for tr in AF['transitions']:
        if tr[0] != nouvel_état:
            AF['transitions'].remove(tr)
            #print(AF)
    supp_état = []
    for i in AF['transitions']:
        supp_état.append(tr[0])
        supp_état.append(tr[2])
    for e in AF['etats']:
        if e not in supp_état:
            AF['etats'].remove(e)
    return AF

"""def est_standard(AF):
    if len(AF['initial']) > 1:
        print("Automate non standard")
        a = int(input("Mettez un 1 pour standardiser, 0 sinon: "))
    for tr in AF['transitions']:
        if tr[2] == AF['initial'][0]:
            print("Automate non standard")
            a = int(input("Mettez un 1 pour standardiser, 0 sinon: "))
            break
        if a == 0:
            return "Automate non standard"
        elif a == 1:
            AF = standardisation(AF)
            print("Automate standardisé!")
            return AF"""
def est_standard(AF):
    if len(AF['initial']) > 1:
        return "Automate non standard"
    for tr in AF['transitions']:
        if tr[2] == AF['initial']:
            return "Automate non standard"
    return "automate standard"

a3 = lire_automate_sur_fichier("16")
print(a3)
print(est_standard(a3))
print(standardisation(a3))
print(est_standard(a3))


"- Problème automate 6: Problème d'indice à la suppression de la transition [1, a, 2]"
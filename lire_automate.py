def lecture (automate):
    with open(f"automates/automate{automate}.txt","r") as f:
        a={} #dictionnaire de l'automate
        for ligne in f:
            ligne=ligne.strip()
            if ligne=='transitions:':
                cle=ligne.split(":")[0]
                print(cle)
                a[cle]=[]
                for l in f:
                    l=l.strip()
                    if l=="":
                        break
                    a[cle].append(l.split())
            else :
                cle,valeurs=ligne.split(":")
                a[cle]=valeurs.split()
    return a




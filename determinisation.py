def est_deterministe(AF):
    test=True
    a = AF['alphabet']
    e = AF['etats']
    t = AF['transitions']
    count=0

    if len(AF['initial'])>1: #on vérifie qu'il n'y a pas plusieurs états initiaux
        test=False
        print("Il y a plusieurs états initiaux.")

    if test==True:
        for i in range (len(e)): #on vérifie que chaque état n'a pas plusieurs flèches d'un même symbole
            for j in range (len(a)):
                for k in range (len(t)):
                    if t[k][0]==e[i] and t[k][1]==a[j]:
                        count+=1
                if count>1:
                    test=False
                    print("L'état",e[i],"a plusieurs flèches",a[j],)
                count=0

    if test==False:
        print("L'automate n'est pas déterministe.")
    else :
        print("L'automate est déterministe.")
    return test


def est_complet (AF):
    test = True
    a = AF['alphabet']
    e = AF['etats']
    t = AF['transitions']
    count = 0

    for i in range(len(e)):
            for k in range(len(t)):
                if t[k][0] == e[i] :
                    count += 1
            if count !=len(a):
                test = False
                print("L'état", e[i], "n'a pas une flèche pour chaque symbole.")
            count = 0

    if test == False:
        print("L'automate n'est pas complet.")
    else:
        print("L'automate est complet.")
    return test


def completion (AF):
    AF["etats"].append("P")
    a = AF['alphabet']
    e = AF['etats']
    t = AF['transitions']
    check=False

    for i in range(len(e)):
        for j in range(len(a)):
            check=False
            for k in range(len(t)):
                if t[k][0]==e[i] and t[k][1]==a[j]:
                    check=True
            if check==False:
                t.append([e[i],a[j],"P"])


    return AF

def determinisation_et_completion (AF):
    AFD={'etats':[],'alphabet':[],'initial':[],'final':[],'transitions':[]}
    AFD['alphabet']=AF['alphabet']
    initial=""

    for i in range (len(AF['initial'])):
        if initial=="":
            initial=AF['initial'][i]
        else :
            initial=initial+"."+AF['initial'][i]

    AFD['initial'].append(initial)
    AFD['etats'].append(initial)

    e=AFD['etats']
    a=AFD['alphabet']
    t1=AF['transitions']
    t2=AFD['transitions']
    f=AFD['final']

    j=0

    while j<len(e):
        for k in range (len(a)):
            fin=""
            for l in range (len(t1)):
                etats=e[j].split(".")
                for w in range(len(etats)):
                    if t1[l][0]==etats[w] and t1[l][1]==a[k] :
                        if t1[l][2] not in fin:
                            if fin=="":
                                fin=t1[l][2]
                            else :
                                fin=fin+"."+t1[l][2]
            if fin!="":
                if fin not in e:
                    e.append(fin)
                t2.append([e[j],a[k],fin])
        j+=1

    for i in range (len(AF['final'])):
        for j in range(len(e)):
            check=False
            etats = e[j].split(".")
            for k in range(len(etats)):
                if etats[k] in AF['final']:
                    check=True
            if check and e[j] not in f:
                f.append(e[j])

    if est_complet(AFD)==False:
        AFDC=completion(AFD)
    else:
        AFDC=AFD
    return AFDC

def afficher_automate_deterministe_complet(AFDC):
    #afficher_automate(AFDC)
    for i in range (len(AFDC['etats'])):
        print(AFDC['etats'][i], end="")
        e=AFDC['etats'][i].split(".")
        print(" <- {", end="")
        for j in range (len(e)):
            print(e[j], end="")
            if j!=len(e)-1:
                print(",", end="")
        print("} de l'automate original")





